import csv
import re
import string
def count_degrees(csv_file_name):
    with open(csv_file_name, 'rt') as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = [row[1] for row in reader]
        faculty = list(rows)
    
    newdata = [re.sub("[.]", "", x) for x in faculty]
    counts = dict()
    degrees = ['MD', 'MA', 'ScD', 'BSEd', 'PhD', '0', 'MPH', 'MS', 'JD']
    for l in degrees:
        counts[l] = [(n.count(l)) for n in newdata].count(1)
    return counts

print(count_degrees('faculty.csv'))
def count_titles(csv_file_name):
    with open(csv_file_name, 'rt') as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = [row[2] for row in reader]
        faculty = list(rows)

    title_counts = dict()
    titles = ['Professor', 'Associate', 'Assistant']
    for l in titles:
        title_counts[l] = [(n.count(l)) for n in faculty].count(1)
    title_counts['Professor'] = len(faculty) - (title_counts['Associate'] + title_counts['Assistant'])
    return title_counts

print(count_titles('faculty.csv'))
def emails(csv_file_name):
    with open(csv_file_name, 'rt') as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = [row[3] for row in reader]
        email_list = list(rows)
    return email_list
def find_domains(email_list):
    email = [re.sub(r'.*@', '', x) for x in email_list]
    return set(email)

email_list = emails('faculty.csv')
print(find_domains(email_list))

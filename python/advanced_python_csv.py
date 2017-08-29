import csv
def emails(csv_file_name):
    with open(csv_file_name, 'rt') as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = [row[3] for row in reader]
        email_list = list(rows)
    return email_list
def write_to_csv(list_of_emails):
    with open('emails.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['here is my header'])
        for i in list_of_emails:
            writer.writerow([i])
emails_to_write = emails('faculty.csv')
write_to_csv(emails_to_write)

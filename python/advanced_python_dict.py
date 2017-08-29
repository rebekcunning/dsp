facultycsv = 'faculty.csv'
import csv
from itertools import islice
def get_dict():
    with open('faculty.csv', mode='r') as infile:
        reader = csv.reader(infile)
        infile.readline()
        mydict = {}
        for row in reader:
            lastname = row[0].split()[-1]
            mydict[lastname] = [row[1:]]
        return mydict   

answer = get_dict()
def get_dict_names():
    with open('faculty.csv', mode='r') as infile:
        reader = csv.reader(infile)
        infile.readline()
        mydict = {}
        for row in reader:
            name = tuple([row[0].split()[-1], row[0].split()[0]])
            mydict[name] = row[1:]
    return mydict

dict_firstnames = get_dict_names()
print(dict_firstnames)
def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))
print(take(3, dict_firstnames.items()))


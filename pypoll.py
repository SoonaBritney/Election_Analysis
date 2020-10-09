# Module for reading CSV files
import csv
import os

#csvpath = os.path.join('', 'Resources', 'election_results.csv')

# Module for reading CSV files
import csv

#assign a variable
file_to_load = os.path.join("resources", "election_results.csv")

# assign a file to save
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open the election file to read
with open(file_to_load) as election_data:

#read the file object with reader function
    file_reader = csv.reader(election_data)
    print(election_data)

# print the header
    headers = next(file_reader)
    print(headers)


#print each row in the csv file
    for row in file_reader:
        print(row)



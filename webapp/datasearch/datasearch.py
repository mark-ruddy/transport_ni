import csv
import sys

#input number you want to search
string = 'Dunnamanagh'
#read csv, and split on "," the line
csv_file = csv.reader(open('datasearch/Dataset.csv', "r"), delimiter=",")


#loop through the csv list
for row in csv_file:
    #if current rows 2nd value is equal to input, print that row
    if string == row[0]:
         print (row)

import xlrd
import requests
import json
import pandas
import csv

#ISO-8859-1
with open("v1.csv", encoding='utf-8',errors='ignore') as f:
    csvDictreader = csv.DictReader(f)
    #csv_reader = csv.DictReader((line.replace('\0', '') for line in f), delimiter=",")
    for row in csvDictreader:
        print(type(row))
        print(row)


import csv
import os
import sys
from csv import reader
#finding number of unique restaurants in the dataset to know if it needs to be larger or smaller
unique_list = []
with open('data/yelp_reviews_businesses.csv') as f:
    f.readline()
    csv_data = reader(f)
    for row in csv_data:
        unique_list.append(row[0])
unique_list = list(dict.fromkeys(unique_list))
print(len(unique_list))
#comes out to 1925

#import csv file 
import csv
import os
import statistics

csv_path = os.path.join("Resources", "budget_data.csv")

with open (csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print (csvreader)


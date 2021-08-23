#importing the csv file to python
import csv
import os
import statistics
import sys

csv_path = os.path.join("Resources", "election_data.csv")

with open (csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#identifying the headers of the csv
    csv_header = next(csvreader)

#creating lists for the three data columns in the csv
    voter_id = []
    county = []
    candidate_column = []

#storing csv data into separate variables 
    for rows in csvreader:
        voter_id.append(rows [0])
        county.append(rows [1])
        candidate_column.append(rows [2])

#creating a list of all of the candidates
    candidate_list = []
    candidate_results = {}

#OUTPUT - 1: calculating the total number of votes
    total_votes = len(voter_id)
    print (total_votes)


#OUTPUT - 2: identifying the candidates
    for rows in csvreader:
        candidate_list.append(rows[2])

    name = list(set(candidate_list))

    for person in name:
        result = candidate_list.count(person)
        candidate_results[person] = result
    
    for person in candidate_results.items():
        candidate_results = (result / total_votes) * 100

        if results > 
        

















#creating a function to print the results in terminal
    def financial_analysis():
        print (f"---------------------")
        print (f"Financial Analysis")
        print (f"---------------------")
        print (f"Total Months: {total_months}")
        print (f"Total: ${round(net_profit), 2}")
        print (f"Averaege Change: ${round(average_change), 2}")
        print (f"Greatest Increase in profit: {max_month} (${max_change})")
        print (f"Greatest Decrease in profit: {min_month} (${min_change})")
        print (f"---------------------")

    financial_analysis()

#creating a text file in the Analysis folder and outputting the financial summary of the company 
    text_file = os.path.join("Analysis", "PyBank_Financial_Analsys.txt")

    with open(text_file, mode= "w") as file:
        file.write(
            f"---------------------\n"
            f"Financial Analysis\n"
            f"---------------------\n"
            f"Total Months: {total_months}\n"
            f"Total: ${round(net_profit), 2}\n"
            f"Average Change: ${round(average_change), 2}\n"
            f"Greatest Increase in profit: {max_month} (${max_change})\n"
            f"Greatest Decrease in profit: {min_month} (${min_change})\n"
            f"---------------------\n"
        )
 #informing the user that the calculation is complete and results have been presented in terminal and text file       
        print ("Financial analysis completed")
        print ("---------------------")


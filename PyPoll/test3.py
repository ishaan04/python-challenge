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

#print out the initial headers

    print (f"---------------------")
    print (f"ELECTION RESULTS")
    print (f"---------------------")


#using a dictionary to pick out every single candidate and gathering the total number of values per candidate
    dic = {}
    for cand in candidate_column:
        if cand in dic:
            current_value = dic[cand]
            dic[cand] = current_value + 1
        else:
            dic[cand] = 1

#Calculating the total number of votes
    total_votes = len(voter_id)
    print (f"Total Votes: {total_votes}")
    print (f"---------------------")

# outputting voter percentages
    election_results = ''
    for cand in dic:
        election_results += (cand + ": " + str(round(dic[cand]/total_votes*100,3)) + "% " + "(" + str(dic[cand]) + ")\n")
    election_results = election_results[:-1]
    print (election_results)
    
    print (f"---------------------")

# Identifying the election winner    
    winner = max(dic, key = dic.get)
    
    print (f"WINNER: {winner}")


#creating a text file in the Analysis folder and outputting the election summary into a text file
    text_file = os.path.join("Analysis", "Election_Results.txt")

    with open(text_file, mode= "w") as file:
        
        file.write(
            f"---------------------\n"
            f"ELECTION RESULTS\n"
            f"---------------------\n"
            f"Total Votes: {total_votes}\n"
            f"---------------------\n"
            f"{election_results}\n"
            f"---------------------\n"
            f"WINNER: {winner}\n"
            'Election is completed\n'
            f"---------------------\n"
        )
 #informing the user that the calculation is complete and results have been presented in terminal and text file       
        print ("Election is completed")
        print ("---------------------")






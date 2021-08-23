#importing the csv file to python
import csv
from functools import singledispatch
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

#creating a dictionary to store the candidates and votes
    candidates_name = {}
    candidates_votes = {}
    total_candidate_votes = 0
    winner = 0
    election_winner = ""

#storing csv data into separate variables 
    for rows in csvreader:
        voter_id.append(rows [0])
        county.append(rows [1])
        candidate_column.append(rows [2])


#OUTPUT - 1: calculating the total number of votes
    total_votes = len(voter_id)
    print (total_votes)

#finding out all of the candidates in the data set, and setting the iniital votes for each candidate = 0
    for rows in csvreader:
        candidates_name.append(rows[2])
        total_candidate_votes[rows] = 0

#by continuing on with the loop, if it locates a like-for-like candidate in the column, it will add 1 to the counter (votes against the candidate)
        total_candidate_votes[rows] = total_candidate_votes[rows] + 1

#calculating the statistics summary of the candidate performance
    for summary in total_candidate_votes:
        candidate_performace = total_candidate_votes.get(summary)
        
        performance_percentage = (float(candidate_performace) / float(total_votes)) * 100
     


#identifying the winner from the election
        if candidate_performace > election_winner:
            election_winner = candidate_performace
            election_winner = summary 



#creating a function to print the results in terminal
    def election_results():
        print (f"---------------------")
        print (f"ELECTION RESULTS")
        print (f"---------------------")
        print (f"Total Votes: {total_votes}")
        print (f"---------------------")
        print (f"{performance_percentage} {candidate_performace}")
        print (f"---------------------")
        print (f"WINNER: {election_winner}")

    election_winner()

#creating a text file in the Analysis folder and outputting the election summary into a text file
    text_file = os.path.join("Analysis", "Election_Results.txt")

    with open(text_file, mode= "w") as file:
        file.write(
            f"---------------------\n"
            f"ELECTION RESULTS\n"
            f"---------------------\n"
            f"Total Votes: {total_votes}\n"
            f"---------------------\n"
            f"{performance_percentage} {candidate_performace}\n"
            f"---------------------\n"
            f"WINNER: {election_winner}\n"
            f"---------------------\n"
        )
 #informing the user that the calculation is complete and results have been presented in terminal and text file       
        print ("Election is completed")
        print ("---------------------")






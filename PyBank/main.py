#importing the csv file to python
import csv
import os
import statistics
import sys

csv_path = os.path.join("Resources", "budget_data.csv")

with open (csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#identifying the headers of the csv
    csv_header = next(csvreader)

#creating lists for the two data columns in the csv
    date_column = []
    profit_loss_column = []

#storing csv data into separate variables 
    for rows in csvreader:
        date_column.append(rows [0])
        profit_loss_column.append(int(rows [1]))

#OUTPUT - 1: calculating the number of months/periods
    total_months = len(date_column)
    

#OUTPUT - 2: calculating the net total proft or loss for the company 
    net_profit = sum(profit_loss_column)
    

#OUTPUT - 3: calculating average change of profit and loss for the company
    change = []
    for x in range(1,len(profit_loss_column)):
        item = profit_loss_column[x]
        previous_item = profit_loss_column[x - 1]        
        difference = item - previous_item
        change.append(difference)
        
    average_change = statistics.mean(change)
    

#OUTPUT - 4: calculating the greatest increase and the relative month    
    max_change = max(change)
    index_max = change.index(max_change) + 1
    max_month = date_column[index_max]


#OUTPUT - 5: calculating the greatest decrease and relative month
    min_change = min(change)
    index_min = change.index(min_change) + 1
    min_month = date_column[index_min]


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


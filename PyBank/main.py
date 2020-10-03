# import csv
import os

import csv

#List FinAnalysis variables to solve
Total_Months = []
Total = 0
Average_Change = 0
MoM_Change = 0
Greatest_Increase_Profits = 0
Greatest_Decrease_Profits = 0
Total_Profit_Losses = 0
Last_Profit_Losses = 0



# specify csv file path
csvpath = os.path.join('Resources','budget_data.csv')

#open csv
with open(csvpath) as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

 # Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
     
    # total number of months included in the dataset
        Total_Months+=1

# net total amount of "Profit/Losses" over the entire period
        #Total_Profit_Losses+=int(row[1])

# average of the changes in "Profit/Losses" over the entire period
        #if Total_Months--1:
                
                #Last_Profit_Losses-int(row[1])
       # else:
                #MoM_Change-int(row[1]-Last_Profit_Losses)
                #Total_Change+-MoM_Change
                        

# greatest increase in profits (date and amount) over the entire period


# greatest decrease in losses (date and amount) over the entire period


#Print the analysis 
print(f"Total_Months")
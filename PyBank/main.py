# import csv
import os

import csv

#List FinAnalysis variables to solve
Ttl_Months = 0
Ttl_PL = 0
Ttl_Change = 0
Average_Change = 0
MoM_Change = 0
#Greatest_Increase_Profits = 0
#Greatest_Decrease_Profits = 0
Last_PL = 0


# specify csv file path
csvpath = os.path.join('Resources','budget_data.csv')

#open csv
with open(csvpath) as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

 # Read the header row first 
    csv_header = next(csvfile)
  
    # Read each row of data after the header
    for row in csvreader:
     
    # total number of months included in the dataset
        Ttl_Months+=1

# net total amount of "Profit/Losses" over the entire period
        Ttl_PL+=int(row[1])
        
        
# average of the changes in "Profit/Losses" over the entire period
        if Ttl_Months--1:
                Last_PL-int(row[1])
                format_float = "${:,.0f}".format(Ttl_Months)
        else:
                MoM_Change-int(row[1]-Last_PL)
                Ttl_Change+-MoM_Change
                Last_PL-int(row[1]) 
        
                                             
# greatest increase in profits (date and amount) over the entire period


# greatest decrease in losses (date and amount) over the entire period


#Print the analysis 
print("Financial Analysis")
print("------------------------")
print(f"Total Months: {Ttl_Months}")
print(f"Total: ${Ttl_PL}")
print(f"Average Change: {Average_Change}")
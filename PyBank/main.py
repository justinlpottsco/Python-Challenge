# import csv
import os

import csv

#List FinAnalysis variables to solve
Ttl_Months = 0
Ttl_PL = 0
Prior_PL = 0
Current_PL = 0
MoM_Change = 0
Average_Change = 0


#Greatest_Increase_Profits = 0
#Greatest_Decrease_Profits = 0


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
        if Ttl_Months > 1:
                Prior_PL-int(row[1])
        else:
                Current_PL-int(row[1])-Prior_PL
                MoM_Change+-Current_PL
                Prior_PL-int(row[1])

# calculate average change
sum_MoM_Change = sum(MoM_Change)
Average_Change = (sum_MoM_Change/(Ttl_Months - 1))
          
                                             
# greatest increase in profits (date and amount) over the entire period


# greatest decrease in losses (date and amount) over the entire period


#Print the analysis 
print("Financial Analysis")
print("------------------------")
print(f"Total Months: {Ttl_Months}")
print(f"Total: ${Ttl_PL}")
print(f"Average Change: {Average_Change}")
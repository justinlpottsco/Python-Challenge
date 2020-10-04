# import csv
import os

import csv

#List FinAnalysis variables to solve
Ttl_Months = 0
Ttl_PL = 0
Prior_PL = 0
Change_PL = 0
MoM_Change = 0
Greatest_Increase_Profits = 0
Greatest_Decrease_Profits = 0

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
        if Ttl_Months==1:
                Prior_PL=int(row[1])
        else:
                Change_PL=int(row[1])-Prior_PL
                MoM_Change+=Change_PL
                Prior_PL=int(row[1])

# calculate average change
Average_Change = (MoM_Change/(Ttl_Months-1))
                                                       
# greatest increase in profits (date and amount) over the entire period
if Change_PL>Greatest_Increase_Profits:
        Greatest_Increase_Profits=Change_PL
        #Greatest_Profit_Month=str(row[0])
        
# greatest decrease in losses (date and amount) over the entire period
elif Change_PL<Greatest_Decrease_Profits:
        Greatest_Decrease_Profits=Change_PL
        
        
#Print the analysis 
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {Ttl_Months}")
print(f"Total: ${Ttl_PL}")
print(f"Average Change: {Average_Change}")
print(f"Greatest Increase in Profits: {Greatest_Increase_Profits}")
print(f"Greatest Decrease in Profits: {Greatest_Decrease_Profits}")

#Export to text file folder
csvpath=os.path.join("Analysis","budget_data.txt")
with open(csvpath, "w") as txtfile:

        print("Financial Analysis",file=txtfile)
        print("-------------------------",file=txtfile)
        print(f"Total Months: {Ttl_Months}", file=txtfile)
        print(f"Total: ${Ttl_PL}", file=txtfile)
        print(f"Average Change: {Average_Change}", file=txtfile)
        print(f"Greatest Increase in Profits: {Greatest_Increase_Profits}", file=txtfile)
        print(f"Greatest Decrease in Profits: {Greatest_Decrease_Profits}", file=txtfile)
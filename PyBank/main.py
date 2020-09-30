# import csv
import os

import csv

# specify csv file path
csvpath = os.path.join('Resources','budget_data.csv')

#open csv
with open(csvpath) as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

 # Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)

    
# total number of months included in the dataset


# net total amount of "Profit/Losses" over the entire period


# average of the changes in "Profit/Losses" over the entire period


# greatest increase in profits (date and amount) over the entire period


# greatest decrease in losses (date and amount) over the entire period
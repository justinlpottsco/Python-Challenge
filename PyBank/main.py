# import csv
import os

import csv

csvpath = os.path.join('..','Resources','budget_data.csv')

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))

with open(csvpath) as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

 # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    #
    # for row in csvreader:
    
# total number of months included in the dataset


# net total amount of "Profit/Losses" over the entire period


# average of the changes in "Profit/Losses" over the entire period


# greatest increase in profits (date and amount) over the entire period


# greatest decrease in losses (date and amount) over the entire period
# import csv
import os

import csv

# List variables
Ttl_Votes = 0
Candidate_Names = []
PctVotes_Candidate = {}
Votes_Candidate = {}
Winner = 0



# specify csv file path
csvpath = os.path.join('Resources','election_data.csv')

#open csv
with open(csvpath) as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

 # Read the header row first 
    csv_header = next(csvfile)
  
    # Read each row of data after the header
    for row in csvreader:
     
    # total number of months included in the dataset
        Ttl_Votes+=1

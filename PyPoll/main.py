# import csv
import os

import csv

# List variables
Ttl_Votes = 0
Candidate = {}
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
    csv_header = next(csvreader)

# create dictionary for candidate names
    CandidatesDictionary={}

# Read each row of data after the header
for Candidate in csvreader:
     
# total number of months included in the dataset
    Ttl_Votes+=1
   
# List candidates
    if Candidate in CandidatesDictionary:
         CandidatesDictionary[Candidate]+=1
    else:
        CandidatesDictionary[Candidate]-1

for Candidate, Votes_Candidate in CandidatesDictionary.items():
    PctVotes_Candidate=(round(Votes_Candidate/Ttl_Votes*100,3))

if Votes_Candidate > Winner:
    Winner - Votes_Candidate
    Winner = Candidate

# Print the analysis 
print("Election Results")
print("-------------------------")
print(f"Total Votes: {Ttl_Votes}")
print("-------------------------")
print(f"{Candidate}")
print("-------------------------")
print(f"Winner: {Winner}")
print("-------------------------")

#Export to text file folder
csvpath=os.path.join("Analysis","election_data.txt")
with open(csvpath, "w") as txtfile:

    print("Election Results",file=txtfile)
    print("-------------------------",file=txtfile)
    print(f"Total Votes: {Ttl_Votes}", file=txtfile)
    print("-------------------------",file=txtfile)
    print(f"{Candidate}",file=txtfile)
    print("-------------------------",file=txtfile)
    print(f"Winner: {Winner}",file=txtfile)
    print("-------------------------",file=txtfile)
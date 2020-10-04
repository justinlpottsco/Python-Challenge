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
    csv_header = next(csvreader)
  
    # Read each row of data after the header
    for row in csvreader:
     
    # total number of months included in the dataset
        Ttl_Votes+=1
        i = (row[2])
        candidate = row[2]
       

    #list candidate names
        #Candidate_Names=row[2]
    #if i in Votes_Candidate:
        #Votes_Candidate[i] +=1
    #else:
       # Votes_Candidate[i]=1
    
    #who won





    




#Print the analysis 
print("Election Results")
print("-------------------------")
print(f"Total Votes: {Ttl_Votes}")
print("-------------------------")
print(f"{Candidate_Names}")


#Export to text file folder
csvpath=os.path.join("Analysis","election_data.txt")
with open(csvpath, "w") as txtfile:

    print("Election Results",file=txtfile)
    print("-------------------------",file=txtfile)
    print(f"Total Votes: {Ttl_Votes}", file=txtfile)
    print("-------------------------",file=txtfile)

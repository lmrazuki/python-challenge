# Import modules
import os
import csv

# Open data file
csvpath = os.path.join("..","PyPoll","Resources","election_data.csv")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile,delimiter=",")
    
    csv_header = next(csvreader)

    voter_ids = []
    candidates = []

    for row in csvreader:
         voter_ids.append(row[0])

         if row[2] not in candidates:
            candidates.append(row[2])      

total_votes = len(voter_ids)

def candidate_summary(candidate):
    for row in csvreader:
        
        vote_count = []

        if candidate == row(2):
            vote_count.append(row(0))

    vote_percent = len(vote_count) / total_votes * 100
    return print(f"{candidate}: {vote_percent}% ({vote_count})")

    for candidate in candidates:
        candidate_summary


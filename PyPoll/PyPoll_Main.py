# Import modules
import os
import csv

# Open data file
csvpath = os.path.join("..","PyPoll","Resources","election_data.csv")
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile,delimiter=",")
    
    # skip the header
    csv_header = next(csvreader)

    #establish an empty list
    candidates = {}

    for row in csvreader: 
        
        # setting the name as variable
        name = row[2]

        # defining the {candidate: vote count} value pair
        if name not in candidates:
            candidates[name] =  1
        else:
            candidates[name] += 1
    
    # counting the total votes
    total_votes = sum(candidates.values())

    # sorting the list based on vote count
    sorted_values = sorted(candidates.values())
    sorted_keys = (candidates.keys())
    sorted_values.reverse()
    
    # finding the winning candidate name
    winner = max(candidates, key=candidates.get)


# preparing to write the csv
output_path = os.path.join("..","PyPoll","Output","output.txt")

results = open(output_path,"w+")

# writing the winner
results.write("The winner is " + winner + "\n")

results.write("=========================\n")

# using a for loop to cycle through the candidates and print their values & percentage
for key, value in zip(sorted_keys, sorted_values):
        results.write(f"{key}: {value}" + " (%.2f%%)" % (100*float(value)/total_votes)+ "\n")
    
results.write("=========================\n")

# tallying the final votes and writing
results.write("There were " + str(total_votes) + " votes cast\n")







   

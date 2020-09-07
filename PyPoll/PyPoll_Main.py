# Import modules
import os
import csv

# Open data file
csvpath = os.path.join("..","PyPoll","Resources","election_data.csv")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile,delimiter=",")
    
    csv_header = next(csvreader)

    candidates = {}

    for row in csvreader:
        name = row[2]

        # opening the counter to define the value pair
        if name not in candidates:
            candidates[name] =  1
        else:
            candidates[name] += 1

    print(candidates)
    
    # for key, value in candidates.items()

    # take the key and value of the dictionary and turn in to tuple

    # find the max value from this and return the key





   

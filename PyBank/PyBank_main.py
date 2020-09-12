# Import modules
import os
import csv

# Open data file
csvpath = os.path.join("..","PyBank","Resources","budget_data.csv")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile,delimiter=",")
    
    csv_header = next(csvreader)

    #Setting up the variables
    months = []
    pnl = 0
    max_range = 0
    min_range = 0
    rev_change = []
    revenue = []

    # Forloop to calculate my summaries
    for row in csvreader:

        #Counting the months
        months.append(row[0])

        # Creating a list of revemies tp calculate the change
        revenue.append(float(row[1]))

        # Getting a total of the PnL
        pnl = pnl + int(row[1]) 

        # Finding the greatest month for both value and date
        if int(row[1]) > max_range:
            max_range = int(row[1])
            max_month = row[0]

        # Finding the lowest month for both value and date
        if int(row[1]) < min_range:
            min_range = int(row[1])
            min_month = row[0]

    # Calculating the average
    for i in range(1, len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])   
    average = sum(rev_change)/len(rev_change)
    

# Preparing to write the results in a text file
output_path = os.path.join("..","PyBank","Output","pybank_output.txt")

results = open(output_path,"w+")

# Writing the results, line by line
results.write(f"There are {len(months)} months\n")
results.write(f"The total profit for this period is: ${pnl}\n")
results.write("The average change is: $" +  f"{average:.2f}""\n")
results.write(f"The lowest month was {min_month} with a loss of: ${(min_range)}\n")
results.write(f"The greatest month was {max_month} with a profit of: ${max_range}\n")
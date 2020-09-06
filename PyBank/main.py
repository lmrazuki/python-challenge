import os
import csv

csvpath = os.path.join("..","PyBank","Resources","budget_data.csv")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile,delimiter=",")
    
    csv_header = next(csvreader)

    months = []
    pnl = 0
    max_range = 0
    min_range = 0

    for row in csvreader:

        months.append(row[0])

        pnl = pnl + int(row[1]) 
        
        if int(row[1]) > max_range:
            max_range = int(row[1])
            max_month = row[0]

        if int(row[1]) < min_range:
            min_range = int(row[1])
            min_month = row[0]

    raw_average = 0.00
    raw_average = pnl / len(months)
    average = ("%.2f" % raw_average)

output_path = os.path.join("..","PyBank","Output","output.txt")

results = open(output_path,"w+")

results.write(f"There are {len(months)} months\n")
results.write(f"The total profit for this period is: ${pnl}\n")
results.write(f"The average change is: ${average}\n")
results.write(f"The lowest month was {min_month} with a loss of: ${(min_range)}\n")
results.write(f"The greatest month was {max_month} with a profit of: ${max_range}\n")
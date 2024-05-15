import os
import csv

csvpath = os.path.join('/Users/sanemini/Desktop/Python-challenge/PyPoll/Resources', 'election_data.csv')

if not os.path.isfile(csvpath):
    raise FileNotFoundError(f"CSV file not found at path: {csvpath}")

# Reading the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    election = [row for row in csvreader]

# The total number of votes cast

total_votes = len(election)

# The list of candidates who received votes
candidates = {}
for row in election:
    candidate = row[2]
    if candidate in candidates:
        candidates[candidate] += 1
    else:
        candidates[candidate] = 1

#The percentage of votes each candidate won
percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates.items()}

#The total number of votes each candidate won

#The winner of the election based on popular vote
winner = max(candidates, key=candidates.get)

#Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates.items():
    percentage = percentages[candidate]
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Saving the results as txt to the 'analysis' file
output_path = os.path.join('/Users/sanemini/Desktop/Python-challenge/PyPoll/analysis', "election_results.txt")
with open(output_path, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate, votes in candidates.items():
        percentage = percentages[candidate]
        txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")

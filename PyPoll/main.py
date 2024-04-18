import os
import csv

# Path to the CSV file
csv_file_path = os.path.join("..", "resources", "election_data.csv")

#set variables
total_votes = 0
candidate_votes = {}
winning_candidate = 0
winning_total_votes = 0

# open CSV file and read and skip header
with open(csv_file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    for row in csvreader:
        # total votes and candidate list
        total_votes += 1
        candidates = row[2]
        
        # tally the vote count
        if candidates in candidate_votes:
            candidate_votes[candidates] += 1
        else:
            candidate_votes[candidates] = 1

# print the election results
print("Election Results")
print("------------------------")
print(f"Total Votes Cast: {total_votes}")

# calculate and print the percentage and total votes for each candidate
print("------------------------")
#building a list of candidate voted to divide by total for % - googled help with .items
for candidate, votes in candidate_votes.items():
    vote_percentage = (votes / total_votes) * 100
    
    # print the results - mod 3-02 - had to google how to get decimals
    print(f"{candidate}: {vote_percentage:.3f}% ({votes})")
    
    # determine the winning candidate
    if votes > winning_total_votes:
        winning_total_votes = votes
        winning_candidate = candidate

# print the winning candidate
print("------------------------")
print(f"Winner: {winning_candidate}")
print("------------------------")

# Specify the file to write to
output_path = os.path.join("..", "Analysis", "results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the results in analysis file - mod 2-10 & 2-12
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['------------------------'])
    csvwriter.writerow([f"Total Votes Cast: {total_votes}"])
    
    for candidate, votes in candidate_votes.items():
        vote_percentage = (votes / total_votes) * 100
        
        # print the results - mod 3-02 - had to google how to get decimals
        csvwriter.writerow([f"{candidate}: {vote_percentage:.3f}% ({votes})"])
        
        # determine the winning candidate
        if votes > winning_total_votes:
            winning_total_votes = votes
            winning_candidate = candidate

    # print the winning candidate
    csvwriter.writerow(["------------------------"])
    csvwriter.writerow([f"Winner: {winning_candidate}"])
    csvwriter.writerow(["------------------------"])
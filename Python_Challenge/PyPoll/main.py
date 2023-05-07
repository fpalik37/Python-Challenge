import os
import csv

election_data = os.path.join("Resources", "election_data.csv")
election_analysis = os.path.join("analysis", "election_analysis.txt")


# Lists to store data
candidate_choice = []
candidate_votes = {}
total_votes = 0
winning_candidate = " "
winning_count = 0

cand_votes = []
cand_percents = []


# Retrieve election data from csvfile:
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
   
    header = next(csvreader)
    
    for row in csvreader:
    
        # Add candidate
        candidate_name = row[2]
        
        # Add total election votes
        total_votes = total_votes + 1
        
        # Add candidate choice (a reference to the unique set of candidates) and determine vote count for each
        if candidate_name not in candidate_choice:
            candidate_choice.append(candidate_name)
            candidate_votes[candidate_name] = 0         
            
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1    
        
    output=(" \n"
       f"Election Results\n"
        " \n"
        "---------------------------\n"
        " \n"
        f"Total Election Votes Cast: {total_votes}\n"
        " \n"
        "---------------------------\n"
        " \n")
    # Add % vote for each candidate
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        votes_percent = float(votes)/float(total_votes)*100
  
        # Determine election winner
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate  
        
        voter_output = f"{candidate}: {votes_percent:.3f}%  ({votes})\n \n"
        output +=voter_output
  
    output +=f"---------------------------\n \n Winner: {winning_candidate}\n \n ---------------------------\n"

# Set variable for output file
output_file = os.path.join("analysis", "election_analysis.txt")

# Open & write to output file
with open(output_file, "w") as eafile:
    writer = eafile.write
            
    eafile.write(output)
    print(output)









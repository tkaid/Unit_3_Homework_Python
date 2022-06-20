# Import
import os
import csv

#Locating the cvs
election_data = os.path.join ("Data Analytics Course", "python-challenge" "PyPoll" "Resources" "election_data")

# Variables
Count = 0
candidate_list = []
unique_candidate = []
vote_count = []
vote_percent = []

# Open csv
with open('election_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
   
    for row in csvreader:
    
        # Counting the total number of votes
        Count = Count + 1
        
        # Create the candidate list
        candidate_list.append(row[2])
        
        # Create a list from the candidate list to get candidate names
    for C in set(candidate_list):
        unique_candidate.append(C)
        
        # Calcualting The percentage of votes each candidate won
        L = candidate_list.count(C)
        vote_count.append(L)
        
        # Calcualting The total number of votes each candidate won
        T = (L/Count)*100
        vote_percent.append(T)
  
    #The winner of the election based on popular vote.
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]

# Print
print("                       ")
print("Election Results")
print("_______________________")
print("Total Votes :" + str(Count))
print("_______________________")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(round(vote_percent[i],3)) + "% (" + str(vote_count[i])+ ")")
print("_______________________")
print("Winner: " + winner)
print("_______________________")


# Export Results to a txt file
with open('PyPoll.txt', 'w') as text:
    text.write("                        ")
    text.write("Election Results")
    text.write("----------------------\n")
    text.write("Total Vote: " + str(Count))
    text.write("----------------------\n")
    for i in range(len(unique_candidate)):
            (unique_candidate[i] + ": " + str(round(vote_percent[i],3)) + "% (" + str(vote_count[i])+ ")")
    text.write("----------------------\n")
    text.write("Winner: " + winner + "\n")
    text.write("----------------------\n")

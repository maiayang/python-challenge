import os
import csv

budget_csv = os.path.join("Resources", "election_data.csv")

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)

    votes=[]
    diana_degette=0
    raymon_anthony=0
    charles_casper=0

    for row in csvreader:
        #Create a list of all votes
        votes.append(row[2])
    
    #Create a list of candidates
    set_candidates=set(votes)
    list_candidates=list(set_candidates)

    #Tally votes for each candidate
    for vote in votes:     
        if vote=="Diana DeGette":
            diana_degette=diana_degette+1
        elif vote=="Raymon Anthony Doane":
            raymon_anthony=raymon_anthony+1
        elif vote=="Charles Casper Stockham":
            charles_casper=charles_casper+1
    
    total_votes=len(votes)
    percent_diana=round(((diana_degette/total_votes)*100),3)
    percent_raymon=round(((raymon_anthony/total_votes)*100),3)
    percent_charles=round(((charles_casper/total_votes)*100),3)

    if diana_degette > raymon_anthony and diana_degette > charles_casper:
        winner="Diana DeGette"
    elif raymon_anthony > diana_degette and raymon_anthony > charles_casper:
        winner="Raymon Anthony Doane"
    elif charles_casper > diana_degette and charles_casper > raymon_anthony:
        winner="Charles Casper Stockham"
    else:
        winner="It's a Tie"

    #Results
    line_1="Election Results"
    line_2=f"Total Votes: {total_votes}"
    line_3=f"Diana Degette: {percent_diana}% ({diana_degette})"
    line_4=f"Raymon Anthony Doane: {percent_raymon}% ({raymon_anthony})"
    line_5=f"Charles Casper Stockham: {percent_charles}% ({charles_casper})"
    line_6=f"Winner: {winner}"

    #Print to terminal
    print(line_1)
    print(line_2)
    print(line_3)
    print(line_4)
    print(line_5)
    print(line_6)

#Write results to .txt file
output_file = os.path.join("Analysis", "Analysis.txt")

with open(output_file, 'w') as f:
    f.write(line_1)
    f.write('\n')
    f.write(line_2)
    f.write('\n')
    f.write(line_3)
    f.write('\n')
    f.write(line_4)
    f.write('\n')
    f.write(line_5)
    f.write('\n')
    f.write(line_6)


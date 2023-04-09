import os
import csv
# opening the csv file
# I programmed this with the files being located on my c-drive
# the following code will only work if the .py file is in the same directory
# as the resources subfolder
file_name = "election_data.csv"
csvpath = os.path.join(os.getcwd(), "Resources", file_name)
#variables for our analysis
total = 0
s_votes = 0 #Charles Casper Stockham
dd_votes = 0 #Diana DeGette
d_votes = 0 #Raymon Anthony Doane
# read and collect data through the csv file
with open(csvpath, newline="", encoding="utf-8") as elections:
    csvreader = csv.reader(elections, delimiter= ",")
    header = next(csvreader)
    # go through columns and collect data
    for row in csvreader:
        total = total + 1
    #add 1 to candidate vote pools
        if row[2] == "Charles Casper Stockham":
            s_votes = s_votes +1
        elif row[2] == "Raymon Anthony Doane":
            d_votes = d_votes + 1
        elif row[2] == "Diana DeGette":
            dd_votes = dd_votes + 1
# what percentage of votes did the candidate win?
s_percent = (s_votes/total) * 100
d_percent = (d_votes/total) * 100
dd_percent = (dd_votes/total) * 100
# make two lists that we will zip together with the candidate's corresponding
# vote tally
candidate_list = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [s_votes, dd_votes, d_votes]
candidates_votes = dict(zip(candidate_list, votes))
winner = max(candidates_votes, key=candidates_votes.get)
print("Election Results \n----------------------------")
print("Total Votes: " + str(total))
print("----------------------------")
print("Charles Casper Stockham: " + str(round(s_percent, 3)) + "% (" + str(s_votes) + ")")
print("Diana DeGette: " + str(round(dd_percent, 3)) + "% (" + str(dd_votes) + ")")
print("Raymon Anthony Doane: " + str(round(d_percent, 3)) + "% (" + str(d_votes) + ")")
print("----------------------------")
print("Winner: " + winner)
print("----------------------------")

print_txt = os.path.join(os.path.expanduser("~"), "Desktop/PyPoll/Analysis", "election_summary.txt")

with open(print_txt,"w") as file:
    file.write("Election Results\n----------------------------\n")
    file.write("Total Votes: " + str(total))
    file.write("\n----------------------------")
    file.write("\nCharles Casper Stockham: " + str(round(s_percent, 3)) + "% (" + str(s_votes) + ")")
    file.write("\nDiana DeGette: " + str(round(dd_percent, 3)) + "% (" + str(dd_votes) + ")")
    file.write("\nRaymon Anthony Doane: " + str(round(d_percent, 3)) + "% (" + str(d_votes) + ")")
    file.write("\n----------------------------\n")
    file.write("Winner: " + winner)
    file.write("\n----------------------------")
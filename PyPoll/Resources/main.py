# Import dependencies
import os
import csv

# Create path to collect data from research folder
csv_path = os.path.join("..", "Resources", "election_data.csv")

# Create lists
total_votes = []
candidates = []
khan = []
correy = []
li = []
otooley = []

# Open and read csv file
with open(csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    csv_header = next(csv_file)

    # Append info into lists
    for row in csv_reader:
        total_votes.append(row[0])
        candidates.append(row[2])

    # Find votes per person
    for candidate in candidates:
        if candidate == "Khan":
            khan.append(candidates)
            khan_votes = int(len(khan))
        elif candidate == "Correy":
            correy.append(candidates)
            correy_votes = len(correy)
        elif candidate == "Li":
            li.append(candidates)
            li_votes = len(li)
        else:
            otooley.append(candidates)
            otooley_votes = len(otooley)

    # Find voting percentages
    khan_percent = round(((khan_votes / len(total_votes)) * 100), 3)
    correy_percent = round(((correy_votes / len(total_votes)) * 100), 3)
    li_percent = round(((li_votes / len(total_votes)) * 100), 3)
    otooley_percent = round(((otooley_votes / len(total_votes)) * 100), 3)

    # Find winner
    if khan_percent > max(correy_percent, li_percent, otooley_percent):
        winner = "Khan"
    elif correy_percent > max(khan_percent, li_percent, otooley_percent):
        winner = "Correy"
    elif li_percent > max(khan_percent, correy_percent, otooley_percent):
        winner = "Li"
    else:
        winner = "O'Tooley"


# Print results
print('Election Results')
print('-------------------------')
print('Total Votes: {}'.format(len(total_votes)))
print('-------------------------')
print(f'Khan: {khan_percent}% ({khan_votes})')
print(f'Correy: {correy_percent}% ({correy_votes})')
print(f'Li: {li_percent}% ({li_votes})')
print(f"O'Tooley: {otooley_percent}% ({otooley_votes})")
print('-------------------------')
print('Winner: {}'.format(winner))
print('-------------------------')

# Create text file
outpath = os.path.join("..", "Analysis", "election_analysis.txt")

# Write analysis into text file
with open(outpath, 'w') as election_analysis:
    csv_writer = csv.writer(election_analysis)
    election_analysis.write('Election Results')
    election_analysis.write('\n')
    election_analysis.write('-------------------------')
    election_analysis.write('\n')
    election_analysis.write('Total Votes: {}'.format(len(total_votes)))
    election_analysis.write('\n')
    election_analysis.write('-------------------------')
    election_analysis.write('\n')
    election_analysis.write(f'Khan: {khan_percent}% ({khan_votes})')
    election_analysis.write('\n')
    election_analysis.write(f'Correy: {correy_percent}% ({correy_votes})')
    election_analysis.write('\n')
    election_analysis.write(f'Li: {li_percent}% ({li_votes})')
    election_analysis.write('\n')
    election_analysis.write(f"O'Tooley: {otooley_percent}% ({otooley_votes})")
    election_analysis.write('\n')
    election_analysis.write('-------------------------')
    election_analysis.write('\n')
    election_analysis.write('Winner: {}'.format(winner))
    election_analysis.write('\n')
    election_analysis.write('-------------------------')

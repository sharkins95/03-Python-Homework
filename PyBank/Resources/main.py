# import dependencies
import os
import csv

# Create path to collect data from Resources folder
csv_path = os.path.join("..", "Resources", "budget_data.csv")

# Create lists
total_months = []
total_profit = []
date = []
monthly_profit_change = []

# Open and read csv file
with open(csv_path, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvfile)

# Append info into created lists
    for row in csv_reader:

        total_months.append(row[0])
        total_profit.append(int(row[1]))

        # Calculate net profit
        net_profit = sum(total_profit)
        # Append date to list
        date.append(row[0])
        # Calculate date of greatest increase and decrease
        date_increase = total_profit.index(max(total_profit))
        date_decrease = total_profit.index(min(total_profit))

# Find the change from month to month
    for value in range(len(total_profit) - 1):
        
        monthly_profit_change.append(total_profit[value + 1] - total_profit[value])

# Print analysis
print('Financial Analysis')
print('----------------------------')
print("Total Months: {}".format(len(total_months)))
print("Total: ${}".format(net_profit))
print("Average Change: ${}".format(round(sum(monthly_profit_change) / len(monthly_profit_change), 2)))
print("Greatest Increase in Profits: {} (${})".format((date[date_increase]), max(monthly_profit_change)))
print("Great Decrease in Profits: {} (${})".format((date[date_decrease]), min(monthly_profit_change)))

# Create text file
outpath = os.path.join("..", "Analysis", "budget_analysis.txt")

# Write analysis into text file
with open(outpath, 'w') as analysis_file:
    csv_writer = csv.writer(analysis_file)
    analysis_file.write('Financial Analysis')
    analysis_file.write('\n')
    analysis_file.write('----------------------------')
    analysis_file.write('\n')
    analysis_file.write("Total Months: {}".format(len(total_months)))
    analysis_file.write('\n')
    analysis_file.write("Total: ${}".format(net_profit))
    analysis_file.write('\n')
    analysis_file.write("Average Change: ${}".format(round(sum(monthly_profit_change) / len(monthly_profit_change), 2)))
    analysis_file.write('\n')
    analysis_file.write("Greatest Increase in Profits: {} (${})".format((date[date_increase]), max(monthly_profit_change)))
    analysis_file.write('\n')
    analysis_file.write("Great Decrease in Profits: {} (${})".format((date[date_decrease]), min(monthly_profit_change)))
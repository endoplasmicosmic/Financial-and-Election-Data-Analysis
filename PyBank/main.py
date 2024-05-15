import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('/Users/sanemini/Desktop/Python-challenge/PyBank/Resources', 'budget_data.csv')

if not os.path.isfile(csvpath):
    raise FileNotFoundError(f"CSV file not found at path: {csvpath}")


#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period

# Initialize variables
total_months = 0
net_total = 0
changes = []
months = []
greatest_increase = [" ", 0]
greatest_decrease = [" ", 0]

# Open and read in the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    # For the first row
    first_row = next(csvreader)
    total_months += 1
    net_total += int(first_row[1])
    prev_profit = int(first_row[1])
    
    for row in csvreader:
        # Calculating monthly change
        total_months += 1
        net_total += int(row[1])

        change = int(row[1]) - prev_profit
        prev_profit = int(row[1])
        changes.append(change)
        months.append(row[0])

        # Identify the greatest increase and decrease
        if change > greatest_increase[1]:
            greatest_increase = [row[0], change]
        if change < greatest_decrease[1]:
            greatest_decrease = [row[0], change]

# Calculating average change
average_change = sum(changes) / len(changes)

# Print the results
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(net_total))
print("Average Change: $" + str(round(average_change, 2)))
print("Greatest Increase in Profits: " + greatest_increase[0] + " ($" + str(greatest_increase[1]) + ")")
print("Greatest Decrease in Profits: " + greatest_decrease[0] + " ($" + str(greatest_decrease[1]) + ")")

# Saving results to text file
output_path = os.path.join('/Users/sanemini/Desktop/Python-challenge/PyBank/analysis', "financial_analysis.txt")

with open(output_path, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write("Total Months: " + str(total_months) + "\n")
    txtfile.write("Total: $" + str(net_total) + "\n")
    txtfile.write("Average Change: $" + str(round(average_change, 2)) + "\n")
    txtfile.write("Greatest Increase in Profits: " + greatest_increase[0] + " ($" + str(greatest_increase[1]) + ")\n")
    txtfile.write("Greatest Decrease in Profits: " + greatest_decrease[0] + " ($" + str(greatest_decrease[1]) + ")\n")

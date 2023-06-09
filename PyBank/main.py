import os
import csv
# opening the csv file
# I programmed this with the files being located on my c-drive
# the following code will only work if the .py file is in the same directory
# as the resources subfolder
file_name = "budget_data.csv"
csvpath = os.path.join(os.getcwd(), "Resources", file_name)
#arrays for our analysis
months = []
profit = []
profit_change = []
# read and collect data through the csv file
with open(csvpath, newline="", encoding="utf-8") as budget:
    csvreader = csv.reader(budget, delimiter= ",")
    header = next(csvreader)
    # amend arrays to match csv information
    for row in csvreader:
        months.append(row[0])
        profit.append(int(row[1]))
    #average change between months
    for i in range(len(profit)-1):
        profit_change.append(profit[i+1]-profit[i])
# Obtain the max and min of the the montly profit change list
find_increase = max(profit_change)
find_decrease = min(profit_change)
greatest_increase = profit_change.index(max(profit_change)) + 1
greatest_decrease = profit_change.index(min(profit_change)) + 1
# printing to terminal
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(len(months)))
print("Total: " + str(sum(profit)))
print("Average Change: " + str(round(sum(profit_change)/len(profit_change),2)))
print("Greatest Increase in Profits: " + str(months[greatest_increase]) + " $" + (((str(find_increase)))))
print("Greatest Decrease in Profits: " + str(months[greatest_decrease]) + " $" + (((str(find_decrease)))))
# outputting the txt file
# I programmed this with the files being located on my desktop
print_txt = os.path.join(os.path.expanduser("~"), "Desktop/PyBank/Analysis", "bank_summary.txt")
with open(print_txt,"w") as file:
    file.write("Financial Analysis \n---------------------------- \n")
    file.write("Total Months: " + str(len(months)))
    file.write("\nTotal: " + str(sum(profit)))
    file.write("\nAverage Change: " + str(round(sum(profit_change)/len(profit_change),2)))
    file.write("\nGreatest Increase in Profits: " + str(months[greatest_increase]) + " $" + (((str(find_increase)))))
    file.write("\nGreatest Decrease in Profits: " + str(months[greatest_decrease]) + " $" + (((str(find_decrease)))))
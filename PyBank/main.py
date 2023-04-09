import os, csv

# opening the csv file
# I programmed this with the files being located on my desktop,
# so the code was as follows:
# csvpath = os.path.join(path, "C:/Users/MyName/Desktop/budget_data.csv")
path = "/home"
csvpath = os.path.join(path, "C:/Users/ ... /Desktop/PyBank/Resources/budget_data.csv")
#arrays and variables for our analysis
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
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {months[greatest_increase]} (${(str(find_increase))})")
print(f"Greatest Decrease in Profits: {months[greatest_decrease]} (${(str(find_decrease))})")

# outputting the txt file
# I programmed this with the files being located on my desktop,
print_txt = os.path.join(os.path.expanduser("~"), "Desktop/PyBank/Analysis", "bank_summary.txt")

with open(print_txt,"w") as file:
    file.write("Financial Analysis \n---------------------------- \n")
    file.write(f"Total Months: {len(months)} \n")
    file.write(f"Total: ${sum(profit)} \n")
    file.write(f"Average Change: {round(sum(profit_change) / len(profit_change), 2)} \n")
    file.write(f"Greatest Increase in Profits: {months[greatest_increase]} (${(str(find_increase))}) \n")
    file.write(f"Greatest Decrease in Profits: {months[greatest_decrease]} (${(str(find_decrease))}) \n")
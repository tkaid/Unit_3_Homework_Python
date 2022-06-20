# Import
import os
import csv

#Locating the cvs
budget_data = os.path.join("Data Analytics Course","python-challenge" "PyBank" "Resources" "budget_data.csv")

# Open csv
with open('budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

# Variables
    Profits = []
    months = []

    #To miss the frist (header Row)
    for rows in csvreader:
        Profits.append(int(rows[1]))
        months.append(rows[0])

    # Calcualting the profits Change Vaule
    profit_change = []

    for x in range(1, len(Profits)):
        profit_change.append((int(Profits[x]) - int(Profits[x-1])))
    
    # Calculating the average profits change
    profit_average = sum(profit_change) / len(profit_change)
    
    # Calculatign the total months
    Total_months = len(months)

    # Calculating the greatest increase in Profit
    Greatest_increase = max(profit_change)
    
    # Calculating the greatest decrease in Profit
    Greatest_decrease = min(profit_change)


    # Print
    print("                  ")
    print("financial analysis")
    print("-------------------")
    print("Total_months:" + str(Total_months))
    print("Total: " + "$" + str(sum(Profits)))
    print("Average change: " "$" + str(round(profit_average, 2)))
    print("Greatest Increase in Profits: " + str(months[profit_change.index(max(profit_change))+1]) + " " + "$" + str(Greatest_increase))
    print("Greatest Decrease in Profits: " + str(months[profit_change.index(min(profit_change))+1]) + " " + "$" + str(Greatest_decrease))


# Export Results to a txt file
    file = open("pybank.txt","w")
    file.write("financial analysis")
    file.write("-------------------")
    file.write("Total  Months: " + str(Total_months))
    file.write("Total: " + "$" + str(sum(Profits)))
    file.write("Average change: " "$" + str(round(profit_average, 2)))
    file.write("Greatest Increase in Profits: " + str(months[profit_change.index(max(profit_change))+1]) + " " + "$" + str(Greatest_increase))
    file.write("Greatest Decrease in Profits: " + str(months[profit_change.index(min(profit_change))+1]) + " " + "$" + str(Greatest_decrease))
    

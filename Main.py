#PyBank Analysis Script

import os
import csv

#Import CSV file
PyBank = os.path.join("Resources", "budget_data.csv")
with open(PyBank, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

#Lists and variables
    profit = []
    changes = []
    months = []
    count = 0
    profit_total = 0
    profit_differences = 0
    original_profit = 0

#Calculating final results
    for row in csvreader:
        count = count + 1
        months.append(row[0])
        profit.append(row[1])
        profit_total = profit_total + int(row[1])

        concluding_profit = int(row[1])
        monthly_change_profits = concluding_profit - original_profit
        changes.append(monthly_change_profits)

        profit_differences = profit_differences + monthly_change_profits
        original_profit = concluding_profit
        average_profits = monthly_change_profits / count

        greatest_increase = max(changes)
        increase_month = months[changes.index(greatest_increase)]
        greatest_decrease = min(changes)
        decrease_month = months[changes.index(greatest_decrease)]


#Print final results
    print(f'PyBank Analysis')

    print(f'Total Months: {len(months)}')
    print(f'Total: ' + "$" + str(profit_total))
    print(f'Average Change: ' + "$" + str(int(average_profits)))
    print(f'Greatest Increase in Profits: ' + str(increase_month) + " ($" + str(greatest_increase) + ")")
    print(f'Greatest Decrease in Profits: ' + str(decrease_month) + " ($" + str(greatest_decrease) + ")")


#Export results to text file
    with open("Financial_analysis.txt", "w") as text:
        text.write(f'PyBank Analysis' + "\n")

        text.write(f'Total Months: {len(months)}' + "\n")
        text.write(f'Total: ' + "$" + str(profit_total) + "\n")
        text.write(f'Average Change: ' + "$" + str(int(average_profits)) + "\n")
        text.write(f'Greatest Increase in Profits: ' + str(increase_month) + " ($" + str(greatest_increase) + ")\n")
        text.write(f'Greatest Decrease in Profits: ' + str(decrease_month) + " ($" + str(greatest_decrease) + ")\n")























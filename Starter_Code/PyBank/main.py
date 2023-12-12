import csv
import sys
import os

current_dir = os.path.dirname(__file__)
buget_data_path = os.path.join(current_dir, './Resources/budget_data.csv')

total_months = 0
total = 0
change = 0
old_profit_loss = -1
total_change = 0

max_month = ""
max_increase = -sys.maxsize

min_month = ""
max_decrease =  sys.maxsize


with open(buget_data_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        profit_loss = int(row.get('Profit/Losses'))
        total = total + profit_loss
        total_months = total_months + 1

        if old_profit_loss != -1:
            change = profit_loss - old_profit_loss
            if change > max_increase:
                max_increase = change
                max_month = row.get('Date')
            if change < max_decrease:
                max_decrease = change
                min_month = row.get('Date')

            total_change += change

        old_profit_loss = profit_loss


average_change = total_change / (total_months-1)

output = 'Financial Analysis\n'
output += '----------------------------\n'
output += 'Total Months: ' + str(total_months) + '\n'
output += 'Total: $'+str(total) + '\n'
output += 'Average Change: $' + str(average_change) + '\n'
output += 'Greatest Increase In Profits: ' + str(max_month) + ' ($' + str(max_increase) + ')' + '\n'
output += 'Greatest Decrease In Profits: ' + str(min_month) + ' ($' + str(max_decrease) + ')' + '\n'
print(output)
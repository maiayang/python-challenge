import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)

    months=[]
    profit_loss=[]

    for row in csvreader:
        
        #Create a list of months
        months.append(row[0])
        
        #Create a list of profit/losses
        profit_loss.append(int(row[1]))

    #Create a list of changes in profit/loss and calculating average change
    profit_loss_change=[profit_loss[i+1]-profit_loss[i] for i in range(len(profit_loss)-1)]
    average_change=round(sum(profit_loss_change)/len(profit_loss_change),2)

    #Find greatest increase and decrease in profits 
    max_change=max(profit_loss_change)
    min_change=min(profit_loss_change)

    #Use index for max/min values to find corresponding month
    max_index=profit_loss_change.index(max(profit_loss_change))
    max_month=months[max_index+1]

    min_index=profit_loss_change.index(min(profit_loss_change))
    min_month=months[min_index+1]    

    #Results
    line_1="Financial Analysis"
    line_2=f"Total Months: {len(months)}"
    line_3=f"Total: ${sum(profit_loss)}"
    line_4=f"Average Change: ${average_change}"
    line_5=f"Greatest Increase in Profits: {max_month} (${max_change})"
    line_6=f"Greatest Decrease in Profits: {min_month} (${min_change})"
    
    #Print results to terminal   
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

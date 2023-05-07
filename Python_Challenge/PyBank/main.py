import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")

# Lists to store data
mo_yr = []
prof_loss = []


# with open as csvfile:
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
   
    header = next(csvreader)
    
    for row in csvreader:
    
       # Add date
        mo_yr.append(row[0])
        
        # Add profit/loss 
        prof_loss.append(int(row[1])) 
        
                
# Determine total number of months
mo_count = len(mo_yr)
        
# Determine profit/loss change
pl_change = []

for pl in range(1,len(prof_loss)):
    pl_change.append(prof_loss[pl] - prof_loss[pl-1])


# Determine net total profit/losses over entire period
total_pl = sum(prof_loss)

# Determine average of profit/loss change
avg_plc = round(int(sum(pl_change)) / ((mo_count) - 1), 2)

# Determine greatest increase over entire period
greatest_inc = max(pl_change)

# Determine greatest deccrease over entire period
greatest_dec = min(pl_change)
 

# Set variable for output file
output_file = os.path.join("analysis", "budget_analysis.txt")

#  Open the output file
with open(output_file, "w") as bafile:
    writer = bafile.write

    output=(" \n"
         f"Financial Analysis\n"
         " \n"
         "---------------------------\n"
         " \n"
        f"Total Months: {mo_count}\n"
        " \n"
        f"Total: ${total_pl}\n"
        " \n"
        f"Average Change: ${avg_plc}\n"
        " \n"
        f"Greatest Increase: {mo_yr[pl_change.index(greatest_inc)+1]} (${greatest_inc})\n"
        " \n"
        f"Greatest Decrease: {mo_yr[pl_change.index(greatest_dec)+1]} (${greatest_dec})\n" )
    bafile.write(output)
    print(output)
  
    
# Finis!
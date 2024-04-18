import os
import csv

budget_csv = os.path.join("..", "Resources", 'budget_data.csv')


#set variables
Total_Months = 0
Total_Rev = 0
Revenue_Total = []
Revenue_List = []
Max_Diff = ["", 0]
Min_Diff = ["", 99999999999]
Month_List = []
Prev_Value = 0

with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
    #print the header
    print("Financial Analysis")
    print("---------------------------------")

    #calculate outputs
    for row in csvreader:
        #total number of months
        Total_Months += 1
        
        #build current revenue 
        Current_Rev = int(row[1])
        Revenue_Total.append(Current_Rev)

        
        #min/max changes and match month
        if Prev_Value is not 0:
            Revenue_Change = Current_Rev - Prev_Value
            Revenue_List.append(Revenue_Change)
            Month_List.append(row[0])

            #if current change is more than previous max, new max, log month
            if (Revenue_Change > Max_Diff[1]):
                Max_Diff[0] = row[0]
                Max_Diff[1] = Revenue_Change

            #if current change is less than previous min, new min, log month
            if (Revenue_Change < Min_Diff[1]):
                Min_Diff[0] = row[0]
                Min_Diff[1] = Revenue_Change

        Prev_Value = Current_Rev

    #sum values in total revenue list
    Total_Rev = sum(Revenue_Total)
    #calc average by dividing sum of changes by number of changes
    Rev_Avg = sum(Revenue_List) / len(Revenue_List)
   
    print("Total Months: ", Total_Months)
    
    print("Total: $", Total_Rev)

    print("Average Change: $", int(Rev_Avg))

    print(f"Greatest Increase in Profits: {Max_Diff[0]} (${Max_Diff[1]})")

    print(f"Greatest Decrease in Profits: {Min_Diff[0]} (${Min_Diff[1]})")


# Specify the file to write to
output_path = os.path.join("..", "Analysis", "results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the results in analysis file - mod 2-10 & 2-12
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(['------------------------'])
    csvwriter.writerow(["Total Months: ", Total_Months])
    csvwriter.writerow(["Total: $", Total_Rev])
    csvwriter.writerow(["Average Change: $", int(Rev_Avg)])
    csvwriter.writerow([f"Greatest Increase in Profits: {Max_Diff[0]} (${Max_Diff[1]})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {Min_Diff[0]} (${Min_Diff[1]})"])                  
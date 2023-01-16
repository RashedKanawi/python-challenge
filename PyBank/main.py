#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Dependencies
import os
import csv
from pathlib import Path 


total_number_of_months = []
total_profit_Losses = []
monthly_change = []


# In[2]:


#file location
budget_csv = os.path.join("/Users/rashedalkanawi/Desktop/python-challenge/PyBank/Resources/budget_data.csv")


#Open csv in default read mode
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
   #save header
    csv_header = next(csv_file)
    #print header
    print(f"CSV Header: {csv_header}")
    
    for row in csv_reader: 
        total_number_of_months.append(row[0])
        total_profit_Losses.append(int(row[1]))
        


# In[3]:


#monthly profit change between two months. 
for i in range(len(total_profit_Losses)-1):    
    monthly_change.append(total_profit_Losses[i+1]-total_profit_Losses[i])


# In[4]:


#max and min of the the montly change
max_increase_value = max(monthly_change)
max_decrease_value = min(monthly_change)
#display max and min monthly change
max(monthly_change),min(monthly_change)


# In[5]:


#max and min to month using month list and index
max_increase_month = monthly_change.index(max(monthly_change)) + 1
max_decrease_month = monthly_change.index(min(monthly_change)) + 1 


# In[6]:


#Print Statements
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_number_of_months)}")
print(f"Total: ${sum(total_profit_Losses)}")
print(f"Average Change: ${round(sum(monthly_change)/len(monthly_change),2)}")
print(f"Greatest Increase in Profits: {total_number_of_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_number_of_months[max_decrease_month]} (${(str(max_decrease_value))})")


# In[7]:


#The output file
output_file = Path("/Users/rashedalkanawi/Desktop/python-challenge/PyBank/Analysis/Financial_results.txt")


# In[8]:


#print to Financial_Analysis_Summary
with open(output_file,"w") as file:
    file.write("Financial Analysis" + '\n')
    file.write("----------------------------" + '\n')
    file.write(f"Total Months: {len(total_number_of_months)}"+ '\n')
    file.write(f"Total: ${sum(total_profit_Losses)}"+ '\n')
    file.write(f"Average Change: ${round(sum(monthly_change)/len(monthly_change),2)}" + '\n')
    file.write(f"Greatest Increase in Profits: {total_number_of_months[max_increase_month]} (${(str(max_increase_value))})"+ '\n')
    file.write(f"Greatest Decrease in Profits: {total_number_of_months[max_decrease_month]} (${(str(max_decrease_value))})"+ '\n')
    
    


# In[ ]:





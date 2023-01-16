#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Dependencies
import os
import csv
from pathlib import Path 


# In[2]:


#set variables 
total_votes = 0 
Charles_Casper = 0
Diana_DeGette = 0
Raymon_Anthony = 0 


# In[3]:


#file location
election_csv = os.path.join("/Users/rashedalkanawi/Desktop/python-challenge/PyPoll/Resources/election_data.csv")


with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    print(f"CSV Header: {csv_header}")
    
    for row in csv_reader:  
        #Count total votes
        total_votes +=1
        if row[2] == "Charles Casper Stockham": 
            Charles_Casper +=1
        elif row[2] == "Diana DeGette":
            Diana_DeGette +=1
        elif row[2] == "Raymon Anthony Doane": 
            Raymon_Anthony +=1


# In[4]:


#create list contains the candidates and number of votes for each
candidate = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
number_of_votes_for_each = [Charles_Casper, Diana_DeGette ,Raymon_Anthony] 


# In[5]:


#Return the winner using a max function of the dictionary
dict_candidates_and_votes = dict(zip(candidate,number_of_votes_for_each))
winner = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get) 


# In[6]:


#calculate percentage
Charles_percent = (Charles_Casper/total_votes) *100
Diana_percent = (Diana_DeGette /total_votes) * 100
Raymon_percent = (Raymon_Anthony/total_votes)* 100
print(Charles_percent , Diana_percent , Raymon_percent)


# In[7]:


#summary of the analysis
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Charles Casper Stockham: {Charles_percent:.3f}% ({Charles_Casper})")
print(f"Diana DeGette: {Diana_percent:.3f}% ({Diana_DeGette})")
print(f"Raymon Anthony Doane: {Raymon_percent:.3f}% ({Raymon_Anthony})")
print(f"----------------------------")
print(f"Winner: {winner}")
print(f"----------------------------")


# In[8]:


#the output files
output_file = Path("/Users/rashedalkanawi/Desktop/python-challenge/PyPoll/Analysis/Election_Results.txt")


# In[9]:



with open(output_file,"w") as file:
    file.write(f"Election Results"+ '\n')
    file.write(f"----------------------------"+ '\n')
    file.write(f"Total Votes: {total_votes}"+ '\n')
    file.write(f"----------------------------"+ '\n')
    file.write(f"Charles Casper Stockham: {Charles_percent:.3f}% ({Charles_Casper})"+ '\n')
    file.write(f"Diana DeGette: {Diana_percent:.3f}% ({Diana_DeGette})"+ '\n')
    file.write(f"Raymon Anthony Doane: {Raymon_percent:.3f}% ({Raymon_Anthony})"+ '\n')
    file.write(f"----------------------------"+ '\n')
    file.write(f"Winner: {winner}"+ '\n')
    file.write(f"----------------------------")


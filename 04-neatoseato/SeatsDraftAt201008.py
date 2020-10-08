# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

### Pats code - Please dont erase

import math
from queue import PriorityQueue
podsize = 6       # the number of passengers traveling in a group
childcount = 0      
ffmiles = 0       # frequent flyer miles of the group or individual traveling together
ticketnumber = 0  # a way to identify order passengers purchased tickets. 
Customerdata = 1  ### value is to just simulate customer data found in the passengers profile
Childcheck = True ### value is to just simulate customer data found in the passengers profile
Age = 6           ### value is to just simulate customer data found in the passengers profile
Group = 8         ### value is to just simulate customer data found in the passengers profile


class Passenger(object):
    
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority


passenger1 = Passenger("Maude", 5)
passenger2 = Passenger("Barleen", 9)
passenger3 = Passenger("David", 1)
passenger4 = Passenger("Halen" , 3)
passenger5 = Passenger("Van" , 2)
passenger0 = Passenger("Eddy" , 1)
passengers = [passenger4, passenger1, passenger5, passenger3, passenger2, passenger0]


### These lists will hold the passengers that have been sorted to them
GroupwithChildren = []
Group = []
Solo = []
Unaccompanied = []


### It takes in a 'pod' of passengers travelling together (solo or group size).
### and generates a ranking number based on fflyer miles, early ticket purchase,
### and category the passengers fall into. The same number is used for each
### passenger in the group as a means of keeping them together.

### It then does two things:
### 1. Stores the ranking in each passengers profile 
### 2. Creates a list of the passengers in each category

for x in range(0, podsize):
    ffmiles = ffmiles + Customerdata
    if Childcheck:   ### counts number of children in group
        if podsize >1:                    ### Group with children
            childcount = childcount + 1
            Childcheck = True
            Group = 3000000
        else:                             ### Unacompanied Minors
            Group = 1000000
    elif podsize >1:                      ### Group
        Group = 2000000
    else:
        Group = 0                         ### Solo Travelers

### Generates the Ranking number
        
Ranking = (Group + ffmiles + podsize + ticketnumber)


### Assigns the Ranknig to each member in the the 'pod'
print ("Pod check")
print ("Passenger and Ranking")
for x in range(0, podsize):
    passengers[x].priority = Ranking
    print (passengers[x].name , passengers[x].priority)



### This section of code places every passenger into the appropriate list



for x in range(len(passengers)):
 
    if passengers[x].priority < 1000000:
        Solo.append(passengers[x]) 
               
    elif passengers[x].priority < 2000000:
        Unaccompanied.append(passengers[x])
           
    elif passengers[x].priority < 3000000:
        Group.append(passengers[x])
             
    else: 
        GroupwithChildren.append(passengers[x])
      
 

### A print to check that each member has the appropriate priority number.
print ("Check to see if grouping worked")
for x in range(0,len(GroupwithChildren)):
    print (GroupwithChildren[x].name,GroupwithChildren[x].priority)
    
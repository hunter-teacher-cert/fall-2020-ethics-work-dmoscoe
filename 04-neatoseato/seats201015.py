# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 16:02:36 2020

@author: dmosc
"""

###OVERALL PLAN###

#Make a plane, which is a 2D array of seats. (see l 312; make_plane, l 58)
#Create and seat some regular passengers (see l 316; RegularPassengers, l 133)
#Create list of available seats for econ customers, with seat values (see l 319; available_seats, l 120)
#Create some economy customers(see l 322; EconomyPassengers, l 229)
#Rank economy passengers and place them in groups (see l 325; GroupClassification, 289)
#Seat the groups (see l 339-342; Assigners, ll 167-225)
#print the plane (see l 345; 63)


# Izagma's plus
import random

ROWS = 20
COLUMNS = 6
REGULAR = 40
ECONOMY = 40
total_seats = ROWS * COLUMNS

seats = []
passengers = []
assignments = []
GroupWithChildren = []
Group = []
Solo = []
Unaccompanied = []

class Passenger(object):   
    def __init__(self, name, priority, pod, podsize, podtype, age, ticketnumber, ffmiles):
        self.name = name
        self.priority = priority
        self.pod = pod
        self.podsize = podsize
        self.podtype = podtype
        self.age = age
        self.ticketnumber = ticketnumber
        self.ffmiles = ffmiles

class Seat(object):
    def __init__(self, r, c, value):
        letter = ["a","b","c","d","e","f"]
        self.occupied = False;
        # automatically creates the seat's location from the row & column pair
        self.loc = str(r+1) + letter[c] 
        self.value = value
        self.regCustomer = False
        self.pod = 0
 
# creates the plane
def make_plane(rows, columns):
  plane = [[Seat(r,c,100*r+c+1) for c in range(columns)] for r in range(rows)]
  return plane

# prints the plane indicating available seats
def print_plane(plane):
  print("-----------------PLANE---------------------")
  # print the plane seats
  for r in range(len(plane)):
    for c in range(len(plane[0])):
      # add spaces for the aisle
      if c == 3:
        print("      ",end=" ")
      # adjust for smaller row numbers
      if r < 9:
        print("",end=" ")
      print(plane[r][c].loc,end=" ")
      type = "E"
      if plane[r][c].regCustomer:
        type="R"
      # -- indicates available, number indicates occupied
      if plane[r][c].occupied:
        print(type+f"{plane[r][c].pod:03}",end=" ")
      else:
        print("----",end=" ")
    print()

# Occupies the specified seat
def occupy_regular_seat(plane,r,c,pod_number):
  # Only occupy it if it is free,
  # Otherwise return false
  # print(r,c)
  if plane[r][c].occupied:
    return False
  else:
    plane[r][c].occupied = True
    plane[r][c].regCustomer = True
    plane[r][c].pod = pod_number
    return True

def occupy_economy_seat(plane, pod_number, seatIndex):
  # get back seat location from balue
  r = seats[seatIndex]//100
  c = (seats[seatIndex] % 100)-1
  plane[r][c].occupied = True
  plane[r][c].regCustomer = False
  plane[r][c].pod = pod_number

# unoccupy seats
def unoccupy_seat(plane,r,c):
  plane[r][c].occupied = False

# Return number of occupied seats
def occupancy(plane):
  occupied_seats = 0
  for r in range(len(plane)):
    for c in range(len(plane[0])):
      if plane[r][c].occupied:
        occupied_seats += 1
  return occupied_seats 

# List of available seats
def available_seats(plane):
  seats = []
  i = 0
  for r in range(len(plane)):
    for c in range(len(plane[0])):
      if not plane[r][c].occupied:
        seats.append(plane[r][c].value)
      else:
        seats.append(0)
    i += 1
  return seats

# this is the seating of regular customers
def RegularPassengers(numberToSeat):
  # Occupy RnumberToSeat number of regular passangers on the plane
  # Try to seat groups (pods) together
  occupied = 0
  pod_number = 0
  while occupied < REGULAR:
      pod_number += 1
      pod_size = random.randint(0,10)
      # reserve first row for unaccompanied children, last minute, etc.
      r = random.randint(1,ROWS-1)
      c = random.randint(0,COLUMNS-1)
      if pod_size > (COLUMNS-c):
        c -= pod_size - (COLUMNS-c)
        if c < 0:
          c = 0;
      for p in range(pod_size):
          col = c
          row = r
          success = occupy_regular_seat(my_plane,r,c,pod_number)
          if c < COLUMNS-1:
              c += 1
          else:
            if r < ROWS-1:
              r += 1
              c = col - pod_size
              if c < 0:
                c = 0;
            else:
              quit
      occupied = occupancy(my_plane)

# Daniel's

# Izagma - Generalazitation and additions to Daniel's code
def AssignThisGroup(passengers,seats,passengerIndex,seatIndex):
  assignments.append([passengers[passengerIndex], seatIndex])
  occupy_economy_seat(my_plane,passengers[passengerIndex].pod,seatIndex)  #Izagma
  passengers.pop(passengerIndex)
  seats[seatIndex] = 0        # occupied

def GroupsAssigner(passengers,seats):
  # Assumes passengers is a list of Passenger objects. 
  # Assumes seats is a list of seat rankings, where the index of the ranking is interpreted as the seat 
  #   being ranked (e.g., the ranking at index = 0 is the ranking of seat A1). 
  # Returns assignments, a list of [passenger, seatIndex] pairs.
  # A value of 0 in seats represents an occupied seat.

  for i in range(len(passengers)):
        worstRankingPassengerIndex = 0
        worstRankingSeatIndex = 0
        
        for j in range(len(passengers)):
                if passengers[j].priority < passengers[worstRankingPassengerIndex].priority:
                    worstRankingPassengerIndex = j #Find the highest-ranking passenger, who will have the highest priority value.
        
        for k in range(len(seats)):
            if seats[k] > seats[worstRankingSeatIndex]:
                worstRankingSeatIndex = k #Find the worst-ranking seat, which will have the highest priority value.
    
        AssignThisGroup(passengers,seats,worstRankingPassengerIndex,worstRankingSeatIndex)
    
  return assignments

def GroupsWithChildrenAssigner(passengers, seats):  
    return GroupsAssigner(passengers,seats)

def GroupsWithNoChildrenAssigner(passengers, seats):
    # Identical to GroupsWithChildrenAssigner. Only difference is that this should run after GroupsWithChildrenAssigner.
    return GroupsAssigner(passengers,seats)

def SoloAssigner(passengers, seats):
    # Places solo travelers in the best available seats.
    
    for i in range(len(passengers)):
        
        bestRankingSeatIndex = 0
        for h in range(len(seats)):
            if (seats[h] > 0 and bestRankingSeatIndex == 0):
                bestRankingSeatIndex = h
        
        bestRankingPassengerIndex = 0
        
        for j in range(len(passengers)):
            if passengers[j].priority > passengers[bestRankingPassengerIndex].priority:
                bestRankingPassengerIndex = j
        
        for k in range(len(seats)):
            if (seats[k] < seats[bestRankingSeatIndex] and seats[k] != 0):
                bestRankingSeatIndex = k
        
        AssignThisGroup(passengers,seats,bestRankingPassengerIndex,bestRankingSeatIndex)
      
    return assignments

# Izagma
#Create Economy Passengers
def EconomyPassengers(numberToCreate): 
  # Make sure to start the pods passed the Regular passenger pods
  first_pod = REGULAR + 1
  #                      name, priority, pod, podsize, podtype, age, ticketnumber, ffmiles   
  passengers.append(Passenger("Maude", 9, first_pod+3, 2, "GroupWithChildren", 37, 1001, 1000))
  passengers.append(Passenger("Barleen", 9, first_pod+3, 2, "GroupWithChildren", 10, 1002, 1000))
  passengers.append(Passenger("David", 4, first_pod+4, 3, "GroupWithChildren", 30, 1011, 100))
  passengers.append(Passenger("Blitzen", 4, first_pod+4, 3, "GroupWithChildren", 40, 1012, 100))
  passengers.append(Passenger("Cleopatra", 4, first_pod+4, 3, "GroupWithChildren", 5, 1013, 100))
  passengers.append(Passenger("Phyllis", 5, first_pod+9, 1, "Solo", 55, 1020, 2000))
  passengers.append(Passenger("Carl", 3, first_pod+6, 2, "GroupWithNoChildren", 30, 1030, 3000))
  passengers.append(Passenger("Harriet", 3, first_pod+6, 2, "GroupWithNoChildren", 35, 1031, 3000))
  passengers.append(Passenger("Eddie", 8, first_pod+7, 2, "GroupWithNoChildren", 40, 1040, 4000))
  passengers.append(Passenger("Laura", 8, first_pod+7, 2, "GroupWithNoChildren", 39, 1041, 4000))
  passengers.append(Passenger("Steve", 2, first_pod+1, 1, "Solo", 30, 1051, 400))
  passengers.append(Passenger("Joey", 7, first_pod+10, 1, "Unaccompanied", 10, 1060, 900))

# Pat
### It takes in a 'pod' of passengers travelling together (solo or group size).
### and generates a ranking number based on fflyer miles, early ticket purchase,
### and category the passengers fall into. The same number is used for each
### passenger in the group as a means of keeping them together.

### It then does two things:
### 1. Stores the ranking in each passengers profile 
### 2. Creates a list of the passengers in each category
def Ranking(passengers):  

    ffmiles = 0
    childcount = 0
    podsize = len(passengers)
    for x in range(podsize):
        ffmiles += ffmiles
        Childcheck = False
        if passengers[x].age < 14:
            Childcheck = True
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
    Ranking = (Group + ffmiles + podsize)

    ### Assigns the Ranknig to each member in the 'pod'
    # print ("Pod check")
    # print ("Passenger and Ranking")
    for x in range(0, podsize):
      passengers[x].priority = Ranking
    
### This method places every passenger into the appropriate classification list.
### Each list can then be passed to Daniels respective methods.    
 
def GroupClassification (passengers):
    global GroupWithChildren
    global Group
    global Solo
    global Unaccompanied

    for x in range(len(passengers)):
 
        if passengers[x].priority < 1000000:
            Solo.append(passengers[x]) 
               
        elif passengers[x].priority < 2000000:
            Unaccompanied.append(passengers[x])
           
        elif passengers[x].priority < 3000000:
            Group.append(passengers[x])
             
        else: 
            GroupWithChildren.append(passengers[x])

# main
#          0   1   2   3   4   5
letter = ["a","b","c","d","e","f"]
my_plane = make_plane(ROWS,COLUMNS)     # make a plane
# print_plane(my_plane)                   # Print the plane's current Status for Regular customers

#Create and seat some Regular Passengers
RegularPassengers(REGULAR)

# create seats list with values and zero's for occupied seats
seats = available_seats(my_plane)
  
# Create some Economy Passengers
EconomyPassengers(ECONOMY) 

# Rank economy passengers
p = 0 
while p < len(passengers):
  podSize = passengers[p].podsize
  podList = []
  for i in range(podSize):
    podList.append(passengers[p+i])
  Ranking(podList)
  p = p + podSize

# create the groups
GroupClassification(passengers)

# Seat the groups
# Use the Solo assigner for children traveing alone, after that, the first row is available
a = SoloAssigner(Unaccompanied, seats)   
x = GroupsWithChildrenAssigner(GroupWithChildren, seats)    
y = GroupsWithNoChildrenAssigner(Group, seats)
z = SoloAssigner(Solo, seats)

# Print the plane's final status
print_plane(my_plane)
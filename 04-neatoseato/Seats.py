# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 13:59:14 2020

@author: dmosc
"""

class Passenger(object):
    
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

class Seat(object):

    def __init__(self, loc, value):
        self.loc = loc
        self.value = value

def SeatAssigner(passengers, seats):
    """Assumes passengers is a list of Passenger objects. Assumes seats is a list of Seat objects. Returns a dict that matches Passengers to Seats s.t. the highest priority Passengers get the most valuable Seats."""

    assignments = {}
    numberOfPassengers = len(passengers)
    for i in range(numberOfPassengers):
        
        topRankingPassenger = passengers[0]
        topRankingPassengerIndex = 0
        topRankingSeat = seats[0]
        topRankingSeatIndex = 0
        
        for j in range(len(passengers)):
            if passengers[j].priority > topRankingPassenger.priority:
                topRankingPassenger = passengers[j]
                topRankingPassengerIndex = j
    
        for k in range(len(seats)):
            if seats[k].value > topRankingSeat.value:
                topRankingSeat = seats[k]
                topRankingSeatIndex = k
    
        assignments[topRankingPassenger.name] = topRankingSeat.loc
        
        passengers.pop(topRankingPassengerIndex)
        seats.pop(topRankingSeatIndex)

    return assignments

passenger1 = Passenger("Maude", 5)
passenger2 = Passenger("Barleen", 9)
passenger3 = Passenger("David", 4)
seat2A = Seat("2A", 11)
seat3C = Seat("3C", 15)
seat6B = Seat("6B", 13)
seat6A = Seat("6A", 16)

passengers = [passenger1, passenger3, passenger2]
seats = [seat2A, seat3C, seat6A, seat6B]

print(SeatAssigner(passengers, seats))

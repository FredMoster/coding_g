# PATH FINDING
# DIJKSTRA ALGORITHM
# BREADTH-FIRST SEARCH

import sys
import math

class room:
    def __init__(self, exits, money):
        self.exits = exits # set
        self.money = money # int
        self.max_money = 0 # int

rooms = {"E" : room(set(), 0)}

N = int(input())
for i in range(N):
    name, money, e1, e2 = input().split()
    rooms[name] = room({e1, e2}, int(money))

rooms["0"].max_money = rooms["0"].money

sources = {"0"}
while sources:
    source = rooms[sources.pop()]
    for e in source.exits:
        exit = rooms[e]
        exit.max_money = max(exit.max_money, source.max_money + exit.money)
        if e != "E":
            sources.add(e)

print(rooms["E"].max_money)

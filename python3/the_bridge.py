# BACKTRACKING
# DEPTH-FIRST SEARCH

import sys
import math
import copy

nb_bikes = int(input())  # the amount of motorbikes to control
nb_survivors = int(input())  # the minimum amount of motorbikes that must survive

 # L0 to L3 are lanes of the road. A dot character . represents a safe space, a zero 0 represents a hole in the road.
lanes = [input(), input(), input(), input()]

tests = []
actions = ["SPEED", "JUMP", "SLOW", "UP", "DOWN"]
for action1 in actions:
    for action2 in actions:
        for action3 in actions:
            tests.append([action1, action2, action3])


def test_action(bike, action):
    x, y, alive, speed = bike
    if alive != 1: return True
    if action == "SPEED": speed += 1
    elif action == "SLOW":
        if speed == 1: return False
        speed -= 1
    elif action == "UP":
        if y == 0: return False
        y -= 1
    elif action == "DOWN":
        if y == len(lanes)-1: return False
        y += 1
    x += speed

    for i in range(bike[0] + 1, x + 1):
        if i >= len(lanes[y]): break
        if ((action in ["SPEED", "SLOW"] and lanes[y][i] == "0")
            or (action == "UP" and (lanes[y][i] == "0" or (i != x and lanes[y+1][i] == "0")))
            or (action == "DOWN" and (lanes[y][i] == "0" or (i != x and lanes[y-1][i] == "0")))
            or (action == "JUMP" and i == x and lanes[y][i] == "0")):
            return False

    bike[0] = x
    bike[1] = y
    bike[3] = speed
    return True


# game loop
while True:
    speed = int(input())  # the motorbikes' speed
    action = "SPEED"

    bikes = []
    for i in range(nb_bikes):
        # x: x coordinate of the motorbike
        # y: y coordinate of the motorbike
        # alive: indicates whether the motorbike is activated "1" or detroyed "0"
        x, y, alive = [int(j) for j in input().split()]
        bikes.append([x, y, alive, speed])

    test_ok = True
    for test in tests:
        curr_bikes = copy.deepcopy(bikes)
        for next_action in test:
            for i in range(nb_bikes):
                test_ok = test_action(curr_bikes[i], next_action)
                if not test_ok: break
            if not test_ok: break
        if test_ok:
            action = test[0]
            break

    print(action)

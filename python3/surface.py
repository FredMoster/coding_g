# MEMOIZATION
# FLOODFILL

import sys
import math

L = int(input())
H = int(input())
MAP = {}
LAKES = {}

def propagate(x, y, lake):
    for a, b in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        if x+a<0 or x+a>H-1 or y+b<0 or y+b>L-1 or x+a not in MAP or y+b not in MAP[x+a] or not MAP[x+a][y+b]:
            continue
        if MAP[x+a][y+b] != lake:
            LAKES[lake] += LAKES[MAP[x+a][y+b]]
            LAKES[MAP[x+a][y+b]] = 0
            MAP[x+a][y+b] = lake
            propagate(x+a, y+b, lake)

for x in range(H):
    row = input()
    MAP[x] = {}
    curr_lake = None
    for y in range(L):
        if row[y] != 'O':
            curr_lake = None
            MAP[x][y] = None
            continue
        if not curr_lake:
            if x>0 and MAP[x-1][y]:
                curr_lake = MAP[x-1][y]
                LAKES[curr_lake] += 1
            else:
                curr_lake = "lake_"+str(len(LAKES.keys()))
                LAKES[curr_lake] = 1
        else:
            LAKES[curr_lake] += 1
        MAP[x][y] = curr_lake
        propagate(x, y, curr_lake)

N = int(input())
for i in range(N):
    x, y = [int(j) for j in input().split()]
    print(0 if not MAP[y][x] else LAKES[MAP[y][x]])

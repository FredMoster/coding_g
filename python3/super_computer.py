# SCHEDULING
# GREEDY ALGORITHM

import sys
import math
import bisect

N = int(input())
reservations = {}
order_end_dates = []

for i in range(N):
    j, d = map(int, input().split())
    end_date = j + d
    if end_date not in reservations:
        reservations[end_date] = j
        bisect.insort(order_end_dates, end_date)
    elif reservations[end_date] < j:
        reservations[end_date] = j

nb_steps = 1
last_end_date = order_end_dates.pop(0)
for next_calc in order_end_dates:
    if reservations[next_calc] >= last_end_date:
        nb_steps += 1
        last_end_date = next_calc

print(nb_steps)

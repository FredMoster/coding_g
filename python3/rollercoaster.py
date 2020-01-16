import sys
import math

L, C, N = [int(i) for i in input().split()]
q = []
for i in range(N):
    q.append(int(input()))

memo = {}

earnings = buffer = 0
for ride in range(C):
    if buffer in memo:
        earnings += memo[buffer][0]
        buffer = memo[buffer][1]
        continue

    seats = group_nb = 0
    front_queue = (group_nb+buffer)%N
    while group_nb < N and seats+q[front_queue] <= L:
        seats += q[front_queue]
        group_nb += 1
        front_queue = (group_nb+buffer)%N
    earnings += seats
    memo[buffer] = (seats, front_queue)
    buffer = front_queue

print(earnings)

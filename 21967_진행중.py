import sys
from collections import deque
from itertools import combinations


input = sys.stdin.readline

n = int(input())


lst = list(map(int, input().split()))

r = 0

if n == 1:
    print(1)
    exit(1)

for i in range(0, n):
    minn = lst[i]
    maxx = lst[i]
    length = 0
    
    for j in range(i, n):
        if minn > lst[j]:
            minn = lst[j]
        if maxx < lst[j]:
            maxx = lst[j]
        if maxx - minn <= 2:
            length += 1
        else:
            break
    if r < length:
        r = length

print(r)
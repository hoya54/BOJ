import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline


x = int(input())

d = deque()

if x == 1:
    print(0)
    exit()

if x%3 == 0:
    d.append(x//3)
if x%2 == 0:
    d.append(x//2)
d.append(x-1)

depth = 0

while d:
    length = len(d)

    for i in range(length):
        t = d.popleft()
        if t == 1:
            d.clear()
            break
        
        if t%3 == 0:
            d.append(t//3)
        if t%2 == 0:
            d.append(t//2)
        d.append(t-1)
        #print(d)

    depth += 1

print(depth)
    
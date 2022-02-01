import sys
from itertools import combinations
from collections import deque


n = int(input())
result = n

state=0

if n-2 >0:
    result += (n-2)
    state = 1

print(result)

if state == 0:
    for i in range(1, n+1):
        print(i, 1)

if state == 1:
    print(1, 1)
    for i in range(2, n):
        print(i, 1)
        print(i, n)
    print(n, 1)
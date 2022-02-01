import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

st = input()

for i in range(n-5, n):
    print(st[i], end='')



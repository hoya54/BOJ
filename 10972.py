import sys
import math
from itertools import permutations

input = sys.stdin.readline


N = int(input())

lst = []

for i in range(N):
    lst.append(i+1)

target = list(map(int, input().split()))

lst.sort(reverse = True)

last = math.factorial(N)

for i in range(N):
    if target[i]
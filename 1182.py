import sys
from itertools import combinations

input = sys.stdin.readline

N, S = map(int, input().split())

lst = list(map(int, input().split()))


ar = []
for i in range(1, N+1):
    for j in combinations(lst, i):
        ar.append(j)

count = 0
for i in ar:
    if sum(i) == S:
        count += 1

print(count)
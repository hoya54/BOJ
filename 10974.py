import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())

lst = []

for i in range(1, N+1):
    lst.append(i)
    
for i in permutations(lst, N):
    print(' '.join(map(str, i)))
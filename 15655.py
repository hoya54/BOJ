import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

lst = list(map(int, input().split()))

lst.sort()

for i in combinations(lst, M):
    print(' '.join(map(str, i)))
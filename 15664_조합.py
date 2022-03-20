import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

lst = list(map(int, input().split()))

lst.sort()
result = combinations(lst, M)
result = set(result)
result = list(result)
result.sort()

for i in result:
    print(' '.join(map(str, i)))

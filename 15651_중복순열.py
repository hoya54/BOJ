import sys
from itertools import product

input = sys.stdin.readline

N, M = map(int, input().split())

lst = []
for i in range(1, N+1):
    lst.append(i)


for i in product(lst, repeat = M):
    print(' '.join(map(str, i)))

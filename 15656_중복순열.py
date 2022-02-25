import sys
from itertools import product

input = sys.stdin.readline

N, M = map(int, input().split())


lst = list(map(int, input().split()))
lst.sort()

for i in product(lst, repeat = M):
    print(' '.join(map(str, i)))
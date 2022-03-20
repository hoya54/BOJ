import sys
from itertools import product

input = sys.stdin.readline

N, M = map(int, input().split())

lst = list(map(int, input().split()))

lst = set(lst)
lst = list(lst)
lst.sort()
result = product(lst, repeat = M)


for i in result:
    print(' '.join(map(str, i)))

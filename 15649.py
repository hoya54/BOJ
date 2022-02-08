import itertools
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

lst = []
for i in range(N):
    lst.append(i+1)

for i in itertools.permutations(lst, M):
    print(' '.join(map(str, i)))

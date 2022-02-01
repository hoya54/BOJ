import sys
import itertools 

input = sys.stdin.readline

N, M = map(int, input().split())

lst = list(map(int, input().split()))


temp = set(itertools.permutations(lst, M))
temp = list(temp)
temp.sort()

for i in temp:
    print(' '.join(map(str, i)))
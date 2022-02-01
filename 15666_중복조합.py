import sys
import itertools 

input = sys.stdin.readline

N, M = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort()

temp = itertools.combinations_with_replacement(lst, M)

temp = set(temp)
temp = list(temp)
temp.sort()


for i in temp:
    print(' '.join(map(str, i)))
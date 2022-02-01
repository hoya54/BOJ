import sys
import itertools 

input = sys.stdin.readline

N, M = map(int, input().split())

lst=[]
for i in range(1, N+1):
    lst.append(i)

for i in itertools.combinations_with_replacement(lst, M):
    print(' '.join(map(str, i)))
import sys
import itertools 

input = sys.stdin.readline

N, M = map(int, input().split())

lst = list(map(int, input().split()))

lst.sort()

for i in itertools.combinations_with_replacement(lst, M):
    print(' '.join(map(str, i)))
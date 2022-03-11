import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))

maxx = -10000000

for i in permutations(lst, N):

    summ = 0
    for j in range(0, N-1):
        summ  += abs(i[j]-i[j+1])
    
    if summ > maxx:
        maxx = summ
print(maxx)
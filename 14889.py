import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())

lst = [[0 for i in range(N)] for j in range(N)]

ar = []
for i in range(N):
    ar.append(i)

for i in range(N):
    st = list(map(int, input().split()))

    for j in range(N):
        lst[i][j] = st[j]


result = []

for i in combinations(ar, N//2):

    temp = []
    for j in ar:
        if j not in i:
            temp.append(j)
    
    start_team = 0
    link_team = 0

    for j in combinations(i, 2):
        a = j[0]
        b = j[1]
        start_team += (lst[a][b] + lst[b][a])

    for j in combinations(temp, 2):
        a = j[0]
        b = j[1]
        link_team +=(lst[a][b] + lst[b][a])
    
    result.append(max(start_team, link_team) - min(start_team, link_team))
    
print(min(result))
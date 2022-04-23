import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

ar = []

for i in range(N):
    st = list(map(int, input().split()))
    ar.append(st)

vacant = []

for i in range(N):
    for j in range(M):
        if ar[i][j] == 0:
            vacant.append((i, j))

vacant_len = len(vacant)
v = [i for i in range(vacant_len)]

max_safe = 0

def dfs(temp, x, y):
    temp[x][y] = 3

    if x-1 >= 0 and temp[x-1][y] == 0:
        dfs(temp, x-1, y)
    if x+1 < N and temp[x+1][y] == 0:
        dfs(temp, x+1, y)
    if y-1 >= 0 and temp[x][y-1] == 0:
        dfs(temp, x, y-1)
    if y+1 < M and temp[x][y+1] == 0:
        dfs(temp, x, y+1)



for i in combinations(v, 3):
    x1, y1 = vacant[i[0]][0], vacant[i[0]][1]
    x2, y2 = vacant[i[1]][0], vacant[i[1]][1]
    x3, y3 = vacant[i[2]][0], vacant[i[2]][1]
    
    temp = [[ 0 for _ in range(M)] for _ in range(N)]
    for j in range(N):
        for k in range(M):
            temp[j][k] = ar[j][k]

    temp[x1][y1] = 1
    temp[x2][y2] = 1
    temp[x3][y3] = 1

    for j in range(N):
        for k in range(M):
            if temp[j][k] == 2:
                dfs(temp, j, k)
    cnt = 0
    for j in range(N):
        for k in range(M):
            if temp[j][k] == 0:
                cnt += 1
    
    if max_safe < cnt:
        max_safe = cnt

print(max_safe)
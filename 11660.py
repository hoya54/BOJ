import sys

input = sys.stdin.readline

N, M = map(int, input().split())

ar = []

for i in range(0, N):
    st = list(map(int, input().split()))
    ar.append(st)

lst = [[0 for col in range(N)] for row in range(N)]

lst[0][0] = ar[0][0]
for i in range(1, N):
    lst[0][i] = lst[0][i-1] + ar[0][i]
    lst[i][0] = lst[i-1][0] + ar[i][0]


for i in range(1, N):
    for j in range(1, N):
        lst[i][j] = ar[i][j] + lst[i-1][j] + lst[i][j-1] - lst[i-1][j-1]


for i in range(0, M):
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1
    x2 -= 1
    y1 -= 1
    y2 -= 1
    
    r= 0
    if x1 >= 1 and y1 >= 1:
        r = lst[x2][y2] - lst[x1-1][y2] - lst[x2][y1-1] + lst[x1-1][y1-1]
    elif x1 >= 1:
        r = lst[x2][y2] - lst[x1-1][y2]
    elif y1 >= 1:
        r = lst[x2][y2] - lst[x2][y1-1]
    else:
        r = lst[x2][y2]
    print(r)
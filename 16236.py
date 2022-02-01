import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

ar=[]
shark_size=2
shark_ate = 0

sx=0
sy = 0

time = 0

for i in range(0, N):
    st = list(map(int, input().split()))
    ar.append(st)

def find_route():
    global ar
    global time
    global shark_ate
    global shark_size
    global sx
    global sy

    temp = [[0 for i in range(N)] for j in range(N)]

    for i in range(0, N):
        for j in range(0, N):
            if ar[i][j] <= shark_size:
                temp[i][j] = -1
            else:
                temp[i][j] = 0

    temp[sx][sy] = 0
    
    d = deque()

    d.append([sx, sy, 0])

    
    sorted_lst=[]
    while d:
        x, y, cnt = d.popleft()
        
        if 0 < ar[x][y] < 9 and ar[x][y] < shark_size:
            sorted_lst.append([temp[x][y], x, y])

        if x-1>=0 and temp[x-1][y] == -1:
            temp[x-1][y]=cnt+1
            d.append([x-1, y, cnt+1])
        if x+1<N and temp[x+1][y] == -1:
            temp[x+1][y]=cnt+1
            d.append([x+1, y, cnt+1])
        if y-1>=0 and temp[x][y-1] == -1:
            temp[x][y-1]=cnt+1
            d.append([x, y-1, cnt+1])
        if y+1<N and temp[x][y+1] == -1:
            temp[x][y+1]=cnt+1
            d.append([x, y+1, cnt+1])

    if len(sorted_lst) == 0:
        return -1
    
    sorted_lst.sort()

    td = sorted_lst[0][0]
    tx = sorted_lst[0][1]
    ty = sorted_lst[0][2]

    ar[sx][sy]=0
    ar[tx][ty]=9

    sx = tx
    sy = ty

    time += td

    shark_ate += 1
    if shark_size == shark_ate:
        shark_size += 1
        shark_ate = 0


for i in range(0, N):
        for j in range(0, N):
            if ar[i][j]==9:
                sx = i
                sy = j
    
while True:

    r = find_route()
    if r == -1:
        break

print(time)
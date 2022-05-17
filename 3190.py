import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

ar = [[0 for _ in range(N+2)] for _ in range(N+2)]
for i in range(N+2):
    ar[0][i] = -1
    ar[N+1][i] = -1
    ar[i][0] = -1
    ar[i][N+1] = -1

k = int(input())
for i in range(k):
    x, y = map(int, input().split())
    ar[x][y] = 4

t = int(input())
lst = deque()
for i in range(t):
    x, y = map(str, input().split())
    lst.append((int(x), y))

time = 0

dir = 0
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

d = deque()
d.append((1, 1))

ar[1][1] = 8

for time in range(1, 10001):
    nx = d[-1][0] + dx[dir]
    ny = d[-1][1] + dy[dir]

    if ar[nx][ny] == -1 or ar[nx][ny] == 8 :
        break
    elif ar[nx][ny] == 4:
        d.append((nx, ny))
        ar[nx][ny] = 8
    else:
        d.append((nx, ny))
        ar[nx][ny] = 8

        tx, ty = d.popleft()
        ar[tx][ty] = 0

    if lst and lst[0][0] == time:
        if lst[0][1] == 'L':
            dir = (dir+1)%4
        else:
            dir = (dir+3)%4

        lst.popleft()

print(time)
# for i in range(N+2):
#     print(ar[i])
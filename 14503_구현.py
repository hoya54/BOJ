import sys

input = sys.stdin.readline

N, M = map(int, input().split())

x, y, d = map(int, input().split())

ar = []
for _ in range(N):
    st = list(map(int, input().split()))
    ar.append(st)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ar[x][y] = 2

while True:
    flag = 0

    for _ in range(4):
        d = (d+3)%4

        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < N and 0 <= ny < M and ar[nx][ny] == 0:
            ar[nx][ny] = 2
            x, y = nx, ny
            flag = 1
            break
        
    if flag == 0:
        if ar[x-dx[d]][y-dy[d]] == 1:
            break
        else:
            x, y = x - dx[d], y - dy[d]

cnt = 0
for i in range(N):
    for j in range(M):
        if ar[i][j] == 2:
            cnt += 1
    #     print(ar[i][j], end='')
    # print()

print(cnt)
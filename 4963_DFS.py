import sys

sys.setrecursionlimit(1000000)

input = sys.stdin.readline



def dfs(ar, w, h, x, y):
    ar[x][y] = 0

    dx = [1, 1, -1, -1,  1, -1,  0,  0]
    dy = [0 ,1,  0,  1, -1, -1,  1, -1]

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < h and 0 <= ny < w and ar[nx][ny] == 1:
            dfs(ar, w, h, nx, ny)    

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    ar = []

    for i in range(h):
        st = list(map(int, input().split()))
        ar.append(st)

    count = 0
    for i in range(h):
        for j in range(w):
            if ar[i][j] == 1:
                dfs(ar, w, h, i, j)
                count += 1
            


    print(count)

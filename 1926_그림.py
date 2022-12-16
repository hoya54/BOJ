

import sys

input = sys.stdin.readline

sys.setrecursionlimit(1000000)

n, m = map(int, input().split())

ar = [[0 for _ in range(m)] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]


for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(m):
        ar[i][j] = lst[j]



dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

w = []
pic_cnt = 0

def dfs(x, y, depth):

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if(0 <= nx < n and 0 <= ny < m and ar[nx][ny] == 1 and visited[nx][ny] == 0):
            visited[nx][ny] = 1
            depth = dfs(nx, ny, depth+1)

    return depth



for i in range(n):
    for j in range(m):
        if(ar[i][j] == 1 and visited[i][j] == 0):
            visited[i][j] = 1
            width = dfs(i, j, 1)
            w.append(width)


print(len(w))
if(len(w) == 0):
    print(0)
else:
    print(max(w))


    
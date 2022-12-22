import sys
from collections import deque

input = sys.stdin.readline

l, w = map(int, input().split())

ar = [[0 for _ in range(w)] for _ in range(l)]


for i in range(l):
    lst = input().strip()

    for j in range(w):
        if(lst[j] == 'W'):
            ar[i][j] = -1
        else:
            ar[i][j] = 1



def bfs(x, y):
    global ar

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    visited = [[0 for _ in range(w)] for _ in range(l)]

    d = deque()

    d.append((x, y, 0)) 
    visited[x][y] = 1
    max_depth = 0

    while d:
        cx, cy, depth = d.popleft()

        max_depth = depth

        for dir in range(4):
            nx = cx + dx[dir]
            ny = cy + dy[dir]

            if(0 <= nx < l and 0 <= ny < w and ar[nx][ny] == 1 and visited[nx][ny] == 0):
                visited[nx][ny] = 1
                d.append((nx, ny, depth+1))

    return max_depth

maxx = 1
for i in range(l):
    for j in range(w):
        if(ar[i][j] == 1):
            maxx = max(maxx, bfs(i, j))

print(maxx)
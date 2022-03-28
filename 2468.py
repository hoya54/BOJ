import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())

ar = []

for i in range(N):
    ar.append(list(map(int, input().split())))

def dfs(visited, i, j, h):
    visited[i][j] = 1

    if i-1 >= 0 and visited[i-1][j] == 0 and ar[i-1][j] > h:
        dfs(visited, i-1, j, h)
    if i+1 <= N-1 and visited[i+1][j] == 0 and ar[i+1][j] > h:
        dfs(visited, i+1, j, h)
    if j-1 >= 0 and visited[i][j-1] == 0 and ar[i][j-1] > h:
        dfs(visited, i, j-1, h)
    if j+1 <= N-1 and visited[i][j+1] == 0 and ar[i][j+1] > h:
        dfs(visited, i, j+1, h)

max_region = 1
for height in range(0, 101):
    num = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and ar[i][j] > height:
                dfs(visited, i, j, height)
                num += 1
    max_region = max(max_region, num)

print(max_region)
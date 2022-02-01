import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline

N = int(input())

ar = [[0 for col in range(N)] for row in range(N)]
visited = [[0 for col in range(N)] for row in range(N)]

ar2 = [[0 for col in range(N)] for row in range(N)]
visited2 = [[0 for col in range(N)] for row in range(N)]
for i in range(0, N):
    st = input()
    for j in range(0, N):
        ar[i][j] = st[j]
        ar2[i][j] = st[j]


for i in range(0, N):
    for j in range(0, N):
        if ar2[i][j] == 'G':
            ar2[i][j] = 'R'

def dfs(ar, visit, x, y):
    global N
    global state

    if visit[x][y]==1:
        return

    visit[x][y]=1

    state=1
    if x+1 <N and ar[x+1][y] == ar[x][y]:
        dfs(ar, visit, x+1, y)
    if y+1 <N and ar[x][y+1] == ar[x][y]:
        dfs(ar, visit, x, y+1)
    if x-1 >= 0 and ar[x-1][y] == ar[x][y]:
        dfs(ar, visit, x-1, y)
    if y-1 >= 0 and ar[x][y-1] == ar[x][y]:
        dfs(ar, visit, x, y-1)

r=0
r2=0
for i in range(0, N):
    for j in range(0, N):
        state=0
        if visited[i][j]==0:
            dfs(ar, visited, i, j)
            r += 1

for i in range(0, N):
    for j in range(0, N):
        state=0
        if visited2[i][j]==0:
            dfs(ar2, visited2, i, j)
            r2 += 1

print(r, r2)

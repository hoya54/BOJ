import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

M, N, K = map(int, input().split())

ar = [[0]*N for _ in range(M)]

for _ in range(K):
    a, b, c, d = map(int, input().split())

    x1, y1 = M-d, a
    x2, y2 =M-b-1, c-1

    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            ar[i][j] = 1

def dfs(x, y):
    global ar
    global cnt

    cnt += 1
    ar[x][y] = 1

    if x-1 >= 0 and ar[x-1][y] == 0:
        dfs(x-1, y)
    if x+1 < M and ar[x+1][y] == 0:
        dfs(x+1, y)
    if y-1 >= 0 and ar[x][y-1] == 0:
        dfs(x, y-1)
    if y+1 < N and ar[x][y+1] == 0:
        dfs(x, y+1)

cnt = 0
lst = []
for i in range(M):
    for j in range(N):
        if ar[i][j] == 0:
            dfs(i, j)
            lst.append(cnt)
            cnt = 0
lst.sort()
print(len(lst))
print(' '.join(map(str, lst)))
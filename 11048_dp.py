import sys

input = sys.stdin.readline

N, M = map(int, input().split())

ar = []
path = []
for i in range(N):
    st = list(map(int, input().split()))
    ar.append(st)
    path.append([0]*len(st))


for i in range(N-1, -1, -1):
    for j in range(M-1, -1, -1):
        if i+1 >= N and j+1 >= M:
            path[i][j] = ar[i][j]
        elif i+1 >= N:
            path[i][j] = ar[i][j] + path[i][j+1]
        elif j+1 >= M:
            path[i][j] = ar[i][j] + path[i+1][j]
        else:
            path[i][j] = ar[i][j] + max(path[i][j+1], path[i+1][j], path[i+1][j+1])
print(path[0][0])
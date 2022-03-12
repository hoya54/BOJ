from glob import glob
import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

N = int(input())

ar = []

for i in range(N):
    ar.append(list(map(int, input().split())))

dp = [[0 for i in range(N)] for j in range(N)]

dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1:
            break

        if i + ar[i][j] < N:
            dp[i + ar[i][j]][j] += dp[i][j]
        if j + ar[i][j] < N:
            dp[i][j + ar[i][j]] += dp[i][j]

print(dp[N-1][N-1])
        
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

lst = []
for i in range(N):
    W, V = map(int, input().split())
    lst.append((W, V, i+1))

for w, v, i in lst:
    for j in range(1, K+1):
        if w > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

# for i in range(1, N+1):
#     print(dp[i][1:])



print(dp[N][K])
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

dp = [100000]*(k+1)

coin = []
for i in range(n):
    t = int(input())

    if t <= k:
        coin.append(t)
        dp[t] = 1


for i in range(1, k+1):
    for j in coin:
        dp[i] = min(dp[i], dp[i-j] + dp[j])

if dp[k] == 100000:
    print(-1)
else:
    print(dp[k])

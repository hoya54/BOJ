import sys

input = sys.stdin.readline

N = int(input())

dp = [0]*(1001)

dp[1] = 1
dp[2] = -1
dp[3] = 1

for i in range(4, N+1):
    dp[i] = max(dp[i-3], dp[i-1])*(-1)


if dp[N] == 1:
    print("SK")
else:
    print("CY")

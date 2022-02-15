import sys
import math

input = sys.stdin.readline

N = int(input())

dp = [0]*(N+1)

for i in range(1, N+1):
    t = int(math.sqrt(i))
    dp[i] = i
    for j in range(1, t+1):
        if dp[i] > 1 + dp[i-j*j]:
            dp[i] = 1 + dp[i-j*j]

print(dp[N])

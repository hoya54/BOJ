import sys

input = sys.stdin.readline

n, k = map(int, input().split())
lst = []
dp = [0]*(k+1)
dp[0] = 1

for i in range(n):
    t = int(input())
    lst.append(t)


for coin in lst:
    for i in range(1, k+1):
        if i - coin >= 0:
            dp[i] += dp[i - coin]



print(dp[k])
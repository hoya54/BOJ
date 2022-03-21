import sys

input = sys.stdin.readline

n = int(input())

lst = []

for i in range(n):
    t = int(input())
    lst.append(t)

dp = [[ 0 for i in range(2)] for j in range(n)]

dp[0] = lst[0]
if n >= 2:
    dp[1] = dp[0] + lst[1]
if n >= 3:
    dp[2] = max(lst[1]+lst[2], lst[0]+lst[2], dp[1])

for i in range(3, n):
    dp[i] = max(dp[i-1], dp[i-3] + lst[i-1] + lst[i], dp[i-2] + lst[i])

print(max(dp))

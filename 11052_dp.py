import sys

input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))

dp = lst[:]

for i in range(N):
    for j in range(i):
        dp[i] = max(dp[i], dp[j]+lst[i-j-1])

print(dp[N-1])
import sys

input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))

dp = [i for i in lst]


for i in range(N):
    for j in range(i):
        if lst[j] < lst[i]:
            dp[i] = max(dp[i], dp[j] + lst[i])
print(max(dp))
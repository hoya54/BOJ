import sys

input = sys.stdin.readline

N = int(input())

lst = []

for i in range(0, N):
    st = list(map(int, input().split()))
    lst.append(st)

dp = [[0, 0, 0] for _ in range(N)]


dp[0][0] = lst[0][0]
dp[0][1] = lst[0][1]
dp[0][2] = lst[0][2]

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + lst[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + lst[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + lst[i][2]
    
print(min(dp[N-1]))
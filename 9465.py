import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    lst = []

    st = list(map(int, input().split()))
    lst.append(st)

    st = list(map(int, input().split()))
    lst.append(st)

    dp = [[0 for _ in range(N)] for _ in range(2)]

    if N >= 1:
        dp[0][0] = lst[0][0]
        dp[1][0] = lst[1][0]
    if N >= 2:
        dp[0][1] = dp[1][0] + lst[0][1]
        dp[1][1] = dp[0][0] + lst[1][1]
    
    
    for i in range(2, N):
        dp[0][i] = max(dp[1][i-1] + lst[0][i], dp[1][i-2] + lst[0][i])
        dp[1][i] = max(dp[0][i-1] + lst[1][i], dp[0][i-2] + lst[1][i])


    print(max(dp[0][N-1], dp[1][N-1]))
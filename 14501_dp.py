import sys

input = sys.stdin.readline

N = int(input())
dp = [0]*(N+6)

lst = []
lst.append([0,0])

for k in range(1, N+1):
    lst.append(list(map(int, input().split())))

for i in range(N, 0, -1):
    length = lst[i][0]
    money = lst[i][1]

    if i+length-1 > N:
        dp[i] = dp[i+1]
    else:
        dp[i] =  max(dp[i+length] + money, dp[i+1])

print(dp[1])
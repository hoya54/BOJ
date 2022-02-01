import sys

input = sys.stdin.readline

X = int(input())

summ=[0]*(X+1)
summ[1]=0

for i in range(2, X+1):
    summ[i] = summ[i-1]+1
    if i%3==0 and summ[i//3]+1 < summ[i]:
        summ[i] = summ[i//3]+1
    if i%2==0 and summ[i//2]+1 < summ[i]:
        summ[i] = summ[i//2]+1

print(summ[X])

# 다른 풀이

# def dp(n):
#     if n in memo:
#         return memo[n]

#     m = 1 + min(dp(n // 2) + n % 2, dp(n // 3) + n % 3)
#     memo[n] = m
#     return m


# memo = {1: 0, 2: 1}
# n = int(input())
# print(dp(n))
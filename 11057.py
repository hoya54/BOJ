import sys

input = sys.stdin.readline

N = int(input())

ar = [[0 for i in range(10)] for j in range(N+1)]

for i in range(10):
    ar[1][i] = 1

for i in range(2, N+1):
    for j in range(0, 10):
        ar[i][j] = sum(ar[i-1][:j+1])

print(sum(ar[N])%10007)
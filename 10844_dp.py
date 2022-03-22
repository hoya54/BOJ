import sys

input = sys.stdin.readline

N = int(input())

lst = [[ 0 for i in range(10)] for j in range(N)]

for i in range(1, 10):
    lst[0][i] = 1

for i in range(1, N):
    lst[i][0] = lst[i-1][1]
    lst[i][9] = lst[i-1][8]

    for j in range(1, 9):
        lst[i][j] = lst[i-1][j-1] + lst[i-1][j+1]

print(sum(lst[N-1])%1000000000)
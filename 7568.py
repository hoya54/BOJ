import sys
input=sys.stdin.readline

N = int(input())

lst = [[0 for col in range(2)] for row in range(N)]

for i in range(0, N):
    a, b = map(int, input().split())
    lst[i][0] = a
    lst[i][1] = b

for i in range(0, N):
    count = 1
    for j in range(0, N):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            count  += 1
    print(str(count) + " ", end="")
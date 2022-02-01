import sys

input = sys.stdin.readline

T = int(input())

def func(ar, a, b):
    sum=0
    for i in range(0, a):
        for j in range(0, b):
            sum = sum + ar[i][j]
    return sum

for i in range(0, T):
    k = int(input())
    n = int(input())

    lst = [[0 for col in range(n)] for row in range(k)]
    for x in range(0, k):
        for y in range(0, n):
            if x==0:
                lst[x][y] = y+1
            else:
                lst[x][y] = func(lst, x, y)
    print(func(lst, k, n))
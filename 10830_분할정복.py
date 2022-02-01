import sys

input = sys.stdin.readline

N, B = map(int, input().split())

lst = []

for i in range(0, N):
    st = list(map(int, input().split()))
    
    lst.append(st)

def power(ar, g):
    temp = [[0 for col in range(N)] for row in range(N)]

    for i in range(0, N*N):
        s = 0
        for j in range(0, N):
            s += ar[i//N][j] * g[j][i%N]
        temp[i//N][i%N] = s%1000
    return temp

def func(ar, t):
    
    if t== 1:
        return ar
    else:
        p = func(ar, t//2)

        if t%2 == 0:
            return power(p, p)
        else:
            return power(p, power(p, lst))
    return ar


r=[[0 for col in range(N)] for row in range(N)]
for i in range(0, N):
    for j in range(0, N):
        r[i][j] = lst[i][j]


r = func(r, B)

for i in range(N):
    for j in range(N):
        print(r[i][j]%1000, end=" ")
    print()
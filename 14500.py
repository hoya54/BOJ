import sys

sys.setrecursionlimit(1000000)

input = sys.stdin.readline

N, M = map(int, input().split())

ar = []

for i in range(0, N):
    st = list(map(int, input().split()))
    ar.append(st)


def func(x, y, summ, depth, v):
    global maxx

    summ  += ar[x][y]

    if depth==4:
        if maxx < summ:
            maxx = summ

        return

    if x-1 >= 0 and v[x-1][y]==0:
        v[x-1][y]=1
        func(x-1, y, summ, depth+1, v)
    if x+1 < N and v[x+1][y]==0:
        v[x+1][y]=1
        func(x+1, y, summ, depth+1, v)
    if y-1 >= 0 and v[x][y-1]==0:
        v[x][y-1]=1
        func(x, y-1, summ, depth+1, v)
    if y+1 < M and v[x][y+1]==0:
        v[x][y+1]=1
        func(x, y+1, summ, depth+1, v)

def func1(x, y):
    global maxx

    if y+3 < M:
        summ = ar[x][y] + ar[x][y+1] + ar[x][y+2] + ar[x][y+3]
        if summ > maxx:
            maxx = summ
    if x+3 < N:
        summ = ar[x][y] + ar[x+1][y] + ar[x+2][y] + ar[x+3][y]
        if summ > maxx:
            maxx = summ


def func2(x, y):
    global maxx

    if x-1 >= 0 and x+1 < N and y-1 >= 0:
        summ=0
        summ = ar[x-1][y] + ar[x+1][y] + ar[x][y-1] + ar[x][y]
        if summ > maxx:
            maxx = summ

    if x+1 < N and x-1 >= 0 and y+1 < M:
        summ=0
        summ = ar[x+1][y] + ar[x-1][y] + ar[x][y+1] + ar[x][y]
        if summ > maxx:
            maxx = summ

    if x-1 >= 0 and y-1 >= 0 and y+1 < M:
        summ=0
        summ = ar[x-1][y] + ar[x][y-1] + ar[x][y+1] + ar[x][y]
        if summ > maxx:
            maxx = summ

    if x+1 < N and  y+1 < M and y-1 >= 0:
        summ=0
        summ = ar[x+1][y] + ar[x][y-1] + ar[x][y+1] + ar[x][y]
        if summ > maxx:
            maxx = summ




def func3(x, y):
    global maxx

    if x+1 < N and y+1 < M:
        summ = ar[x][y] + ar[x][y+1] + ar[x+1][y] + ar[x+1][y+1]
        if summ > maxx:
            maxx = summ

def func4(x, y):
    global maxx

    
    if x+2 < N and y+1 < M:
        a1 = ar[x][y]
        a2 = ar[x][y+1]
        a3 = ar[x+1][y]
        a4 = ar[x+1][y+1]
        a5 = ar[x+2][y]
        a6 = ar[x+2][y+1]
        summ = a1+a2+a3+a4+a5+a6

        s1 = summ - a2 - a4
        if s1 > maxx:
            maxx = s1
        s2 = summ - a4 - a6
        if s2 > maxx:
            maxx = s2
        s3 = summ - a1 - a3
        if s3 > maxx:
            maxx = s3
        s4 = summ - a3 - a5
        if s4 > maxx:
            maxx = s4
        s5 = summ - a2 - a5
        if s5 > maxx:
            maxx = s5
        s6 = summ - a1 - a6
        if s6 > maxx:
            maxx = s6

    if y+2 < M and x+1 < N:
        a1 = ar[x][y]
        a2 = ar[x][y+1]
        a3 = ar[x][y+2]
        a4 = ar[x+1][y]
        a5 = ar[x+1][y+1]
        a6 = ar[x+1][y+2]
        summ = a1+a2+a3+a4+a5+a6

        s1 = summ - a5 - a6
        s2 = summ - a4 - a5
        s3 = summ - a1 - a2
        s4 = summ - a2 - a3
        s5 = summ - a1 - a6
        s6 = summ - a3 - a4
        if s1 > maxx:
            maxx = s1
        if s2 > maxx:
            maxx = s2
        if s3 > maxx:
            maxx = s3
        if s4 > maxx:
            maxx = s4
        if s5 > maxx:
            maxx = s5
        if s6 > maxx:
            maxx = s6

maxx = 0
for i in range(0, N):
    for j in range(0, M):
        func1(i, j)
        func2(i, j)
        func3(i, j)
        func4(i, j)

print(maxx)



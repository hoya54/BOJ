import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())

ar=[]
for i in range(0, N):
    ar.append(list(map(int,input().split())))

cnt_1=0
cnt0=0
cnt1=0

def check(n, x, y):
    global ar

    for i in range(0, n):
        for j in range(0, n):
            if ar[x+i][y+j] != ar[x][y]:
                return 0

    return 1

def func(n, x, y):
    global ar
    global cnt0
    global cnt1
    global cnt_1

    if check(n, x, y):
        tmp = ar[x][y]
        if tmp == 0:
            cnt0 += 1
        elif tmp == -1:
            cnt_1 += 1
        else:
            cnt1 += 1
    else:
        func(n//3, x, y)
        func(n//3, x, y+n//3)
        func(n//3, x, y+2*(n//3))
        func(n//3, x+n//3, y)
        func(n//3, x+n//3, y+n//3)
        func(n//3, x+n//3, y+2*(n//3))
        func(n//3, x+2*(n//3), y)
        func(n//3, x+2*(n//3), y+n//3)
        func(n//3, x+2*(n//3), y+2*(n//3))
            

func(N, 0, 0)
print(cnt_1)
print(cnt0)
print(cnt1)
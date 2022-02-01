import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())

ar = [[0 for col in range(N)] for row in range(N)]

for i in range(0, N):
    st = list(map(int, input().split()))
    for j in range(0, N):
        ar[i][j] = st[j]

cnt0=0
cnt1=0

def func(n, x, y):
    global ar
    global cnt0
    global cnt1

    if n==1:
        if ar[x][y] == 1:
            cnt1 += 1
        else:
            cnt0 += 1
    else:
        flag0=1
        flag1=1

        for i in range(0, n):
            for j in range(0, n):
                if ar[x+i][y+j] !=1:
                    flag1 = 0

        for i in range(0, n):
            for j in range(0, n):
                if ar[x+i][y+j] !=0:
                    flag0 = 0
        if flag0==1:
            
            cnt0 += 1
        elif flag1==1:
            cnt1 +=1
        else:
            func(n//2, x, y)
            func(n//2, x, y+n//2)
            func(n//2, x+n//2, y)
            func(n//2, x+n//2, y+n//2)

func(N, 0, 0)
print(cnt0)
print(cnt1)
import sys
input = sys.stdin.readline

N, M = input().split()
N=int(N)
M=int(M)

#왼쪽 위가 흰색인 체스판
white = [[0 for col in range(8)] for row in range(8)]
for i in range(0, 8):
    for j in range(0, 8):
        if (i+j)%2==0:
            white[i][j]="W"
        else:
            white[i][j]="B"

#왼쪽 위가 흑색인 체스판
black = [[0 for col in range(8)] for row in range(8)]
for i in range(0, 8):
    for j in range(0, 8):
        if (i+j)%2==0:
            black[i][j]="B"
        else:
            black[i][j]="W"

array = [[0 for col in range(M)] for row in range(N)]

for i in range(0, N):
    st = input()
    for j in range(0, M):
        array[i][j] = st[j]
        
minn = 10000000

def func(ar, a, b):
    x=0
    wc=0
    bc=0
    global minn
    for i in range(a, a+8):
        y=0
        for j in range(b, b+8):
            if ar[i][j] != white[x][y]:
                wc +=1
            if ar[i][j] != black[x][y]:
                bc +=1
            y += 1
        x += 1
    if min(wc, bc) < minn:
        minn = min(wc, bc)
    

for i in range(0, N-8+1):
    for j in range(0, M-8+1):
        func(array, i, j)
        
print(minn)
import sys
from collections import deque
sys.setrecursionlimit(1000000)
input=sys.stdin.readline

a, b = map(int, input().split())

ar = []
d = deque()

for i in range(0, b):
    st = list(map(int, input().split()))
    ar.append(st)

for i in range(0, b):
    for j in range(0, a):
        if ar[i][j]==1:
            d.append([i, j])

cnt = 0

def func():
    global ar
    global d
    global a
    global b
    global cnt
    end = len(d)

    if end == 0:
        return
    cnt += 1
    for i in range(0, end):
        temp = d.popleft()
        x = temp[0]
        y = temp[1]
        if x-1 >=0 and ar[x-1][y]==0:
            if ar[x-1][y] == 0:
                ar[x-1][y] = 1
                d.append([x-1, y])
        if y-1 >=0 and ar[x][y-1]==0:
            if ar[x][y-1] == 0:
                ar[x][y-1] = 1
                d.append([x, y-1])
        if x+1 <b and ar[x+1][y]==0:
            if ar[x+1][y] == 0:
                ar[x+1][y] = 1
                d.append([x+1, y])
        if y+1 <a and ar[x][y+1]==0:
            if ar[x][y+1] == 0:
                ar[x][y+1] = 1
                d.append([x, y+1])
        #print(d)
    func()

func()

state=1
for q in range(0, b):
    for r in range(0, a):
        if ar[q][r] == 0:
            state=0
if state == 1:
    print(cnt-1)
else:
    print(-1)

# for q in range(0, b):
#     for r in range(0, a):
#         print(ar[q][r], end=" ")
#     print()
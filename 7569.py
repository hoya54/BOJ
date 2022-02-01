import sys
from collections import deque
sys.setrecursionlimit(1000000)
input=sys.stdin.readline

a, b, c = map(int, input().split())

ar = []

d = deque()
for j in range(0, c):
    arr=[]
    for i in range(0, b):
        st = list(map(int, input().split()))
        arr.append(st)
    ar.append(arr)

#print(ar)
for k in range(0, c):
    for i in range(0, b):
        for j in range(0, a):
            if ar[k][i][j]==1:
                d.append([k, i, j])

cnt = 0

def func():
    global ar
    global d
    global a
    global b
    global c
    global cnt
    end = len(d)

    if end == 0:
        return
    cnt += 1
    for i in range(0, end):
        temp = d.popleft()
        x = temp[0]
        y = temp[1]
        z = temp[2]
        if x-1 >=0 and ar[x-1][y][z]==0:
            if ar[x-1][y][z] == 0:
                ar[x-1][y][z] = 1
                d.append([x-1, y, z])
        if y-1 >=0 and ar[x][y-1][z]==0:
            if ar[x][y-1][z] == 0:
                ar[x][y-1][z] = 1
                d.append([x, y-1, z])
        if z-1 >=0 and ar[x][y][z-1]==0:
            if ar[x][y][z-1] == 0:
                ar[x][y][z-1] = 1
                d.append([x, y, z-1])

        if x+1 <c and ar[x+1][y][z]==0:
            if ar[x+1][y][z] == 0:
                ar[x+1][y][z] = 1
                d.append([x+1, y,z])
        if y+1 <b and ar[x][y+1][z]==0:
            if ar[x][y+1][z] == 0:
                ar[x][y+1][z] = 1
                d.append([x, y+1, z])
        
        if z+1 <a and ar[x][y][z+1]==0:
            if ar[x][y][z+1] == 0:
                ar[x][y][z+1] = 1
                d.append([x, y, z+1])
        #print(d)
    func()

#print(d)
func()
#print(ar)
state=1
for k in range(0, c):
    for q in range(0, b):
        for r in range(0, a):
            if ar[k][q][r] == 0:
                state=0
if state == 1:
    print(cnt-1)
else:
    print(-1)

# for q in range(0, b):
#     for r in range(0, a):
#         print(ar[q][r], end=" ")
#     print()
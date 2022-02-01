import sys
from collections import deque
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, M= map(int, input().split())

ar = [[0 for col in range(M)] for row in range(N)]

for i in range(0, N):
    st = input()
    for j in range(0, M):
        ar[i][j] = int(st[j])*(-1)


minn = 999999
def bfs():
    global ar
    global N
    global M

    d = deque()
    d.append([0,0, 1])

    while d:
        x, y, cnt = d.popleft()
        cnt = cnt+1

        if x-1>=0 and ar[x-1][y]==-1:
            ar[x-1][y]=cnt
            d.append([x-1, y, cnt])
        if x+1<N and ar[x+1][y]==-1:
            ar[x+1][y]=cnt
            d.append([x+1, y, cnt])
        if y-1>=0 and ar[x][y-1]==-1:
            ar[x][y-1]=cnt
            d.append([x, y-1, cnt])
        if y+1<M and ar[x][y+1]==-1:
            ar[x][y+1]=cnt
            d.append([x, y+1, cnt])
        
ar[0][0]=1

bfs()

print(ar[N-1][M-1])

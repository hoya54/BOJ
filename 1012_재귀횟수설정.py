import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)
T = int(input())
count=0
visited =[]

def func(ar, x, y):
    global visited
    global count

    if visited[x][y]==1 or ar[x][y]==0:
        return
    else:
        visited[x][y]=1
        count += 1

    if x-1 >=0 and ar[x-1][y]==1:
        func(ar, x-1, y)
    if y-1 >=0 and ar[x][y-1]==1:
         func(ar, x, y-1)
    if x+1 <N and ar[x+1][y]==1:
         func(ar, x+1, y)
    if y+1 <M and ar[x][y+1]==1:
         func(ar, x, y+1)



result = []
for t in range(0, T):
    M, N, K = map(int, input().split())
    ar = [[0 for col in range(M)] for row in range(N)]
    visited = [[0 for col in range(M)] for row in range(N)]

    for k in range(0, K):
        a, b = map(int, input().split())
        ar[b][a]=1
    cnt=0

    for i in range(0, N):
        for j in range(0, M):
            count=0
            func(ar, i, j)
            if count !=0:
                cnt +=1       
    result.append(cnt)

for i in range(0, T):
    print(result[i])


import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)
N = int(input())
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
    if y+1 <N and ar[x][y+1]==1:
         func(ar, x, y+1)

result = []
ar = [[0 for col in range(N)] for row in range(N)]
visited = [[0 for col in range(N)] for row in range(N)]

for t in range(0, N):
    s = input()
    for i in range(0, N):
        ar[t][i]=int(s[i])


for i in range(0, N):
    for j in range(0, N):
        count=0
        func(ar, i, j)
        if count !=0:
            result.append(count)   

print(len(result))
result.sort()
for i in range(0, len(result)):
    print(result[i])


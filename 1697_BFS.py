import sys
from collections import deque
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

a, b = map(int, input().split())

d = deque()

deep=0
visited=[0]*100001
def func(b):
    global d
    global deep
    global s
    
    end = len(d)

    
    while d:
        temp = d.popleft()
        
        if temp == b:
            return visited[temp]

        x1 = temp - 1
        x2 = temp +1
        x3 = temp*2

        if 0 <= x1 <= 100000 and visited[x1]==0:
            visited[x1]=visited[temp]+1
            d.append(x1)
        if 0 <= x2 <= 100000 and visited[x2]==0:
            visited[x2]=visited[temp]+1
            d.append(x2)
        if 0 <= x3 <= 100000 and visited[x3]==0:
            visited[x3]=visited[temp]+1
            d.append(x3)


d.append(a)
visited[a]=0

if a==b:
    print(0)
else:
    print(func(b))
import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(1000000)
N, M = map(int, input().split())

ar = []
visited = [0]*101
for i in range(0, 101):
    ar.append(i)

for i in range(0, N):
    a, b = map(int, input().split())
    ar[a] = b

for i in range(0, M):
    a, b = map(int, input().split())
    ar[a] = b


d = deque()
cnt=-1

def func():
    global ar
    global d
    global cnt

    lst=[]
    lst.append(1)

    while d:
        cnt += 1
        
        end = len(d)

        for i in range(0, end):
            n = d.popleft()
            
            if n==100:
                return

            for j in range(1, 7): 
                if n+j <= 100 and (n+j) not in lst:
                    if n+j != ar[n+j]:
                        d.append(ar[n+j])
                        lst.append(ar[n+j])
                        lst.append(n+j)
                    else:
                        d.append(n+j)
                        lst.append(n+j)

d.append(1)

func()
print(cnt)
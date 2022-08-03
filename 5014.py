import sys
from collections import deque

inut = sys.stdin.readline


full, start, destination, u, d = map(int, input().split())

diff = destination - start

visited = [0]*(full+1)

q = deque()

q.append((start, 0))
visited[start] = 1

flag = 0

while q:
    cur, cnt = q.popleft()

    #print(cur, cnt)

    if cnt > 1000000:
        break

    if cur == destination:
        print(cnt)
        flag = 1
        break

    

    if cur+u <= full and visited[cur+u] == 0:
        visited[cur+u] = 1
        q.append((cur+u, cnt+1))
    if 1 <= cur-d and visited[cur-d] == 0:
        visited[cur-d] = 1
        q.append((cur-d, cnt+1))
    

if flag == 0:
    print("use the stairs")

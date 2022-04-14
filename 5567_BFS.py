import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

g = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())

    g[a][b] = 1
    g[b][a] = 1

visited = [0]*(n+1)

q = deque()

q.append(1)
visited[1] = 1

connected_to_1 = sum(g[1])

for _ in range(connected_to_1+1):
    t = q.popleft()
    for i in range(2, n+1):
        if g[t][i] == 1 and visited[i] == 0:
            visited[i] = 1
            q.append(i)

print(sum(visited) - 1)
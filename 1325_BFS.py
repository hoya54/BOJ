from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]


def BFS(x, visited):
    cnt = 1

    queue = deque()

    queue.append(x)
    visited[x] = 1

    while queue:
        t = queue.popleft()

        for i in (graph[t]):
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                cnt += 1


    return cnt


for _ in range(M):
    x, y = map(int, input().split())

    graph[y].append(x)


ar = [0]*(N+1)

for i in range(1, N+1):
    visited = [0]*(N+1)
    c = BFS(i, visited)
    ar[i] = c

maxx = max(ar)
r = []
for i in range(1, N+1):
    if ar[i] == maxx:
        r.append(i)

print(' '.join(map(str, r)))



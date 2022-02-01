import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())

start = int(input())

graph = [[] for _ in range(V+1)]

distance = [INF]*(V+1)


for i in range(0, E):
    u, v, w = map(int, input().split())

    graph[u].append((w, v))
    

distance[start] = 0

h = []
heapq.heappush(h, (0, start))

while h:
    cur_weight, now = heapq.heappop(h)

    if distance[now] < cur_weight:
        continue

    for w, next in graph[now]:
        temp = w + cur_weight
        if temp < distance[next]:
            distance[next] = temp
            heapq.heappush(h, (temp, next))

for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
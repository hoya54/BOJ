import sys
import heapq
INF = sys.maxsize

input = sys.stdin.readline


N, E = map(int, input().split())

graph = [[] for i in range(N+1)]

for i in range(E):
    a, b, c = map(int, input().split())

    graph[a].append((b, c))
    graph[b].append((a, c))

m1, m2 = map(int, input().split())

def func(start, end):

    distance = [INF]*(N+1)
    distance[start] = 0

    h = []
    heapq.heappush(h, (0, start))

    while h:
        cur_weight, now = heapq.heappop(h)

        if distance[now] < cur_weight:
            continue

        for next, w in graph[now]:
            temp = w + cur_weight
            if temp < distance[next]:
                distance[next] = temp
                heapq.heappush(h, (temp, next))
                
    distance[0] = -1
    return distance[end]

bewteen_m12 = func(m1, m2)

m1_m2 = func(1, m1) + bewteen_m12 + func(m2, N) 

m2_m1 = func(1, m2) + bewteen_m12 + func(m1, N)

result = min(m1_m2, m2_m1)

if result < INF:
    print(result)
else:
    print(-1)

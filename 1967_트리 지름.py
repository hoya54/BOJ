import sys
import heapq
INF = sys.maxsize

input = sys.stdin.readline


N = int(input())

graph = [[] for i in range(N+1)]

for i in range(N-1):
    p, c, w = map(int, input().split())

    graph[p].append((c, w))
    graph[c].append((p, w))


def func(start):

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
    return distance.index(max(distance))

def func2(start, end):

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

start = func(1)
end = func(start)

result = func2(start, end)

print(result)


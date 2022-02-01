import sys
import heapq

input = sys.stdin.readline

N = int(input())

graph = [[-1 for col in range(N+1)] for row in range(N+1)]

visited = [0]*(N+1)
distance = [999999999]*(N+1)

M = int(input())

for i in range(0, M):
    start, end, time = map(int, input().split())
    if graph[start][end] != -1:
        if graph[start][end] > time:
            graph[start][end] = time
    else:
        graph[start][end] = time

tstart, tend = map(int, input().split())
distance[tstart] = 0


for i in range(1, N+1):

    minn=999999999
    minn_num = 0
    for j in range(1, N+1):
        if visited[j] == 0 and minn > distance[j]:
            minn = distance[j]
            minn_num = j
    s = minn_num
    visited[s] = 1

    for j in range(1, N+1):
        if distance[s] + graph[s][j] < distance[j] and graph[s][j] != -1:
            distance[j] = distance[s] + graph[s][j]


# 우선순위 큐 사용
# h = []
# heapq.heappush(h, [0, tstart])

# while h:
#     s = heapq.heappop(h)[1]

#     if visited[s] == 1:
#         continue
#     visited[s] = 1

#     for j in range(1, N+1):
#         if distance[s] + graph[s][j] < distance[j] and graph[s][j] != -1:
#             distance[j] = distance[s] + graph[s][j]
#             heapq.heappush(h, [distance[j], j])
    

print(distance[tend])
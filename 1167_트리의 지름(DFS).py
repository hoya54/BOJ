import sys
import heapq
INF = sys.maxsize

input = sys.stdin.readline


N = int(input())

graph = [[] for i in range(N+1)]

for i in range(1, N+1):
    st = list(map(int, input().split()))

    j=1
    while True:
        if st[j] == -1:
            break
        graph[st[0]].append((st[j], st[j+1]))
        #graph[st[j]].append((i, st[j+1]))
        j += 2



def dfs(start, g, result):
    for edge, weight in g[start]:
        if result[edge] == 0:
            result[edge] = result[start] + weight
            dfs(edge, g, result)

# 트리의 1번 노드에서 가장 먼 노드 x 찾기
result1 = [0] * (N+1)
dfs(1, graph, result1)
x = result1.index(max(result1))


# x에서 가장 먼 노드 찾기
result2 = [0] * (N+1)
dfs(x, graph, result2)
result2[x]=0 #출발지는 0으로 처리
y = max(result2) 

print(y)
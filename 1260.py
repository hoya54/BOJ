import sys
from collections import deque
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, M, V = map(int, input().split())

ar = [[0 for col in range(N+1)] for row in range(N+1)]
visited_dfs = [0]*(N+1)
visited_bfs = [0]*(N+1)
result_bfs=[]
result_dfs=[]



def bfs(t):
    global ar
    global visited_bfs
    global N
    
    d = deque()

    d.append(t)

    while len(d) != 0:

        target = d.popleft()
        for i in range(1, N+1):
            if ar[target][i]==1 and visited_bfs[i]==0:
                visited_bfs[i]=1
                result_bfs.append(i)
                d.append(i)

            

def dfs(t):
    global ar
    global visited_dfs
    global N

    for i in range(1, N+1):
        if ar[t][i]==1 and visited_dfs[i]==0:
            visited_dfs[i]=1
            result_dfs.append(i)
            dfs(i)




for i in range(0, M):
    a, b = map(int, input().split())
    ar[a][b] = 1
    ar[b][a] = 1
visited_dfs[V]=1
result_dfs.append(V)
dfs(V)

visited_bfs[V]=1
result_bfs.append(V)
bfs(V)

for i in range(0, len(result_dfs)):
    print(result_dfs[i], end=" ")
print()
for i in range(0, len(result_bfs)):
    print(result_bfs[i], end=" ")


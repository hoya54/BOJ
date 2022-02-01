import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline

N = int(input())

lst = [[] for j in range(N+1)]

visited = [0]*(N+1)

for i in range(2, N+1):
    a, b = map(int, input().split())

    lst[a].append(b)
    lst[b].append(a)

dic={}

def dfs(n):
    visited[n] = 1

    for i in lst[n]:
        if visited[i] == 0:
            dic[i] = n
            dfs(i)
dfs(1)

for i in range(2, N+1):
    print(dic[i])
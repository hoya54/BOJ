import sys

input = sys.stdin.readline

T = int(input())



for t in range(T):
    N, M = map(int, input().split())
    ar = [[0 for i in range(N+1)] for j in range(N+1)]
    for i in range(M):
        a, b = map(int, input().split())
        ar[a][b] = 1
        ar[b][a] = 1
    print(N-1)
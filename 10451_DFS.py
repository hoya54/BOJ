import sys

input = sys.stdin.readline

T = int(input())

cycle = 0


for _ in range(T):
    N = int(input())

    lst = list(map(int, input().split()))

    dic = {}

    for i in range(N):
        dic[i+1] = lst[i]
    
    visited = [0] * (N+1)

    cycle = 0

    for i in range(1, N+1):
        if visited[i] != 0:
            continue

        visited[i] = i
        next = dic[i]
        while i != next:
            visited[next] = next
            next = dic[next]
        cycle += 1

    print(cycle)

        


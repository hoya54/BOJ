import sys

from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

def bfs():
    visited = [200000]*100001
    ways = [0]*100001
    
    d = deque()

    d.append(N)

    ways[N] = 1
    visited[N] = 0

    cnt = 0
    success = False

    while d:
        end = len(d)

        for _ in range(0, end):
            current = d.popleft()
            
            for j in [current-1, current+1, current*2]:
                if 0 <= j <= 100000 and cnt +1 <= visited[j]:
                    #print(j)
                    ways[j] += 1
                    visited[j] = cnt+1

                    if j == K:          # 가장 처음 이 조건을 만족하면 다음 깊이는 안보기 위함
                        success = True

                    if not success:
                        d.append(j)
        cnt += 1
    # print()
    # for i in range(1, 7):
    #     print(ways[i], end=' ')
    # print()
    # for i in range(1, 7):
    #     print(visited[i], end=' ')
    # print()
    return visited[K], ways[K]

time, count = bfs()


print(time)
print(count)
import sys
from collections import deque

input = sys.stdin.readline

dirx = [-1, -2, -2, -1, 1, 2,  2,  1]
diry = [-2, -1,  1,  2, 2, 1, -1, -2]

T = int(input())

for _ in range(T):
    N = int(input())
    
    ar = [[1 for _ in range(N)] for _ in range(N)]

    cur_x, cur_y = map(int, input().split())
    target_x, target_y = map(int, input().split())
    
    ar[cur_x][cur_y] = 0

    if cur_x == target_x and cur_y == target_y:
        print(0)
        continue

    d = deque()

    d.append((cur_x, cur_y, 0))

    while d:
        
        cur_x, cur_y, depth = d.popleft()

        if cur_x == target_x and cur_y == target_y:
            print(depth)
            break

        for i in range(8):
            nx = cur_x + dirx[i]
            ny = cur_y + diry[i]

            if 0 <= nx < N and 0 <= ny < N and ar[nx][ny] == 1:
                ar[nx][ny] = 0
                d.append((nx, ny, depth+1))

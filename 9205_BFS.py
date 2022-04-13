import sys
import copy
from collections import deque

input = sys.stdin.readline

t = int(input())

def dist(a, b, x, y):
    return abs(a-x) + abs(b-y)

def find(x, y, dx, dy, bottles, stores):
    # 바로 갈 수 있다면
    if dist(x, y, dx, dy) <= bottles*50:
        return True
    
    # 바로는 못감, 편의점 들러야함
    for i in range(len(stores)):
        sx, sy, visited = stores[i][0], stores[i][1], stores[i][2]
        if visited == 1:
            continue

        if dist(x, y, sx, sy) <= bottles*50:
            copied_stores = copy.deepcopy(stores)
            copied_stores[i][2] = 1
            result = find(sx, sy, dx, dy, 20, copied_stores)
            if result == True:
                return True
        
    return False

def BFS():
    q = deque()
    q.append([x1, y1])

    while q:
        x, y = q.popleft()
        if dist(x, y, destx, desty) <= 1000:
            print("happy")
            return
        
        for i in range(n):
            if visited[i] == 0:
                nx, ny = stores[i]
                if dist(x, y, nx, ny) <= 1000:
                    q.append([nx, ny])
                    visited[i] = 1
    
    print("sad")


for _ in range(t):
    n = int(input())

    x1, y1 = map(int, input().split())
    b = 20

    stores = []
    for i in range(n):
        sx, sy = map(int, input().split())
        stores.append([sx, sy]) # x, y, visited

    destx, desty = map(int, input().split())

    visited = [0]*(n+1)

    BFS()


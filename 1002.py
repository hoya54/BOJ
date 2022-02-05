import sys
import math

input = sys.stdin.readline

T = int(input())


for k in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    d = math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

    if d == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    elif d+min(r1, r2) <= max(r1, r2):
        if d + min(r1, r2) < max(r1, r2):
            print(0)
        elif d + min(r1, r2) == max(r1, r2):
            print(1)
        else:
            print(2)
    else:
        if d == r1+r2:
            print(1)
        elif d > r1+r2:
            print(0)
        else:
            print(2)
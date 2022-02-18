import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    count = 0
    N = int(input())
    for j in range(N):
        cx, cy, r = map(int, input().split())
        r1 = (x1-cx)**2 + (y1-cy)**2 - r**2
        r2 = (x2-cx)**2 + (y2-cy)**2 - r**2
        if  r1*r2 < 0:
            count += 1
    
    print(count)





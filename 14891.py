import sys
from collections import deque

input = sys.stdin.readline

a = deque(map(int, input().rstrip()))
b = deque(map(int, input().rstrip()))
c = deque(map(int, input().rstrip()))
d = deque(map(int, input().rstrip()))

k = int(input())

def rotate(target, dir):
    if dir == 1:
        target.appendleft(target.pop())
    else:
        target.append(target.popleft())
    

for i in range(k):
    n, dir = map(int, input().split())

    bench = []
    if n == 1:
        bench.append((a, dir))
        if a[2] != b[6]:
            bench.append((b, -dir))
            if b[2] != c[6]:
                bench.append((c, dir))
                if c[2] != d[6]:
                    bench.append((d, -dir))
    elif n == 2:
        bench.append((b, dir))
        if a[2] != b[6]:
            bench.append((a, -dir))
        if b[2] != c[6]:
            bench.append((c, -dir))
            if c[2] != d[6]:
                bench.append((d, dir))
    elif n == 3:
        bench.append((c, dir))
        if c[2] != d[6]:
            bench.append((d, -dir))
        if b[2] != c[6]:
            bench.append((b, -dir))
            if a[2] != b[6]:
                bench.append((a, dir))
    else:
        bench.append((d, dir))
        if c[2] != d[6]:
            bench.append((c, -dir))
            if b[2] != c[6]:
                bench.append((b, dir))
                if a[2] != b[6]:
                    bench.append((a, -dir))
    
    for temp in bench:
        rotate(temp[0], temp[1])
    
print(a[0]*1 + b[0]*2 + c[0]*4 + d[0]*8)

        
    

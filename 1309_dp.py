import sys

input = sys.stdin.readline

N = int(input())

t0 = 1 
t1 = 1
tx = 1

for i in range(1, N):
    t0, t1, tx = (t1+tx)%9901, (t0+tx)%9901, (t0+t1+tx)%9901

print((t0 + t1 + tx)%9901)

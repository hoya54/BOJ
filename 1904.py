import sys

input = sys.stdin.readline

N = int(input())

a = 1
b = 2
c = 0

for i in range(3, N+1):
    c = (a + b)%15746
    a = b
    b = c

if N < 3:
    print(N)
else:
    print(c)
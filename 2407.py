import sys

input = sys.stdin.readline

a, b = map(int, input().split())

x=1
for i in range(a, a-b, -1):
    x = x*i
y=1
for i in range(1, b+1):
    y = y*i
print(x//y)
import sys
input = sys.stdin.readline

a, b = input().split()

c = a[::-1]
d = b[::-1]
c = int(c)
d = int(d)

print(max(c, d))
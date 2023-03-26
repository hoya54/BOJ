import sys


input = sys.stdin.readline

n = int(input())

l = 1
r = 1

d = 1

depth = 1
remain = 0

for i in range(n-1):
    if remain == 0:
        if d == 1:
            r += 1
        else:
            l += 1
        remain = depth
        depth += 1
        d = (d+1)%2
    else:
        if d == 1:
            l -= 1
            r += 1
        else:
            l += 1
            r -= 1
        remain -= 1

print(l, end='')
print('/', end='')
print(r, end='')

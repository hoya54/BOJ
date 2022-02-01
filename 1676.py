import sys

input = sys.stdin.readline

N = int(input())

r=1
for i in range(N, 0, -1):
    r = r*i

s=0

a = str(r)
for i in range(len(a)-1, 0, -1):
    if a[i]=='0':
        s += 1
    else:
        break
print(s)
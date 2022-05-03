import sys

input = sys.stdin.readline

st = input().rstrip()

n = len(st)

i = 0
while i < n:
    for j in range(i, min(i+10, n)):
        print(st[j], end='')
    i += 10
    print()


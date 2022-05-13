import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    lst = list(input().split())
    r = []

    for word in lst:
        r.append(word[::-1])
    print(' '.join(map(str, r)))
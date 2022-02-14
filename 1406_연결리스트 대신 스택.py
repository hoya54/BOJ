import sys
from collections import deque

input = sys.stdin.readline

st = input().rstrip()

l = deque()
r = deque()

for i in st:
    l.append(i)

N = int(input())

for i in range(N):
    lst = list(map(str, input().split()))

    if lst[0] == 'L':
        if len(l) == 0:
            continue
        r.appendleft(l.pop())
    elif lst[0] == 'D':
        if len(r) == 0:
            continue
        l.append(r.popleft())
    elif lst[0] == 'B':
        if len(l) != 0:
            l.pop()
    else:
        lst[1].rstrip()
        l.append(lst[1])

print(''.join(map(str, l+r)))

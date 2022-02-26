import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

for i in range(N):
    ld = deque()
    rd = deque()

    st = input().rstrip()
    for j in range(len(st)):
        if st[j] == '-':
            if len(ld) == 0:
                pass
            else:
                ld.pop()
        elif st[j] == '<':
            if len(ld) == 0:
                pass
            else:
                rd.appendleft(ld.pop())
        elif st[j] == '>':
            if len(rd) == 0:
                pass
            else:
                ld.append(rd.popleft())
        else:
            ld.append(st[j])
    print(''.join(map(str, ld+rd)))

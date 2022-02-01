import sys
input = sys.stdin.readline
N = int(input())

from collections import deque

d = deque()

for i in range(0, N):
    st = input().split()
    if st[0] == "push_front":
        d.appendleft(st[1])

    if st[0] == "push_back":
        d.append(st[1])

    elif st[0] == "pop_front":
        if len(d)==0:
            print(-1)
        else:
            print(d.popleft())
    elif st[0] == "pop_back":
        if len(d)==0:
            print(-1)
        else:
            print(d.pop())

    elif st[0] == "size":
        print(len(d))

    elif st[0] == "empty":
        if len(d) == 0:
            print(1)
        else:
            print(0)
            
    elif st[0] == "front":
        if len(d)==0:
            print(-1)
        else:
            print(d[0])
    
    elif st[0] == "back":
        if len(d)==0:
            print(-1)
        else:
            print(d[-1])
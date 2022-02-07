import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

lst = map(int, input().split())
lst = list(lst)


c = 0
d = deque()
for i in range(1, N+1):
    d.append(i)


for i in lst:
    if i == d[0]:
        N -= 1
        d.popleft()

    else:
        index = 0
        for j in range(len(d)):
            if d[j] == i:
                index = j+1
                break
        if index-1 < N+1-index:
            c += index-1
            for k in range(index-1):
                d.append(d.popleft())
        else:
            c += N+1-index
            for k in range(N+1-index):
                d.appendleft(d.pop())
        d.popleft()
        N -= 1

print(c)


# deque.rotate(1)
# 양수면 오른쪽 으로 숫자만큼 회전
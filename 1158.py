from collections import deque

N, K = map(int, input().split())

lst = [i for i in range(1, N+1)]
result = []

cnt = 0
for i in range(N):
    cnt += K-1
    cnt = cnt % len(lst)
    result.append(lst.pop(cnt))

print('<', end='')
print(', '.join(map(str, result)), end='')
print('>', end='')
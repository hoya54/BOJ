import sys

input = sys.stdin.readline

N, K = map(int, input().split())

lst=[]
for i in range(0, N):
    lst.append(int(input()))

cnt=0
for i in range(len(lst)-1, -1, -1):
    if lst[i] > K:
        continue
    else:
        cnt += K // lst[i]
        K = K%lst[i]

print(cnt)
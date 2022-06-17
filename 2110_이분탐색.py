import sys

input = sys.stdin.readline

n, c = map(int, input().split())

lst = []
for i in range(n):
    x = int(input())
    lst.append(x)

lst.sort()

left = 1

right = lst[-1]
result = 0
while left <= right:
    mid = (left+right)//2
    

    cnt = 1
    cur = lst[0]
    for i in range(1, len(lst)):
        if lst[i] - cur >= mid:
            cnt += 1
            cur = lst[i]
    #print(left, right, cnt)
    if cnt >= c:
        left = mid + 1
        result = mid
    else:
        right = mid - 1

print(result)



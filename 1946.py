import sys

input = sys.stdin.readline

T = int(input())

result = []
for _ in range(T):
    N = int(input())

    lst = []
    for _ in range(N):
        x, y = map(int, input().split())
        lst.append((x, y))
    lst.sort()

    minn = lst[0][1]
    cnt = 1

    for i in range(1, N):  
        if lst[i][1] < minn:
            cnt += 1
            minn = lst[i][1]

    result.append(cnt)

    

for i in result:
    print(i)



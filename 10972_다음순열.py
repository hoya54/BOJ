import sys

input = sys.stdin.readline


N = int(input())

lst = list(map(int, input().split()))

index = -1

for i in range(N-1, 0, -1):
    if lst[i-1] < lst[i]:
        index = i-1
        break

if index == -1:
    print(index)
else:
    for i in range(N-1, 0, -1):
        if lst[index] < lst[i]:
            tmp = lst[i]
            lst[i] = lst[index]
            lst[index] = tmp

            result = lst[:index+1] + sorted(lst[index+1:])
            print(*result)
            break

import sys

input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))

result = [1]*N


for i in range(0, N):
    for j in range(0, i):
        if lst[j] < lst[i]:
            result[i] = max(result[i], result[j]+1)
print(max(result))
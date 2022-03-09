import sys

input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))

result = [1]*N


for i in range(N):
    for j in range(i):
        if lst[j] > lst[i]:
            result[i] = max(result[j]+1, result[i])

print(max(result))
 

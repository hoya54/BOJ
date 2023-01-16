import sys

input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))

ar = [sys.maxsize]*(n+1)

for i in range(1, n+1):
    num = lst[i-1]
    ar[i] = min(ar[i], lst[i-1])
    for j in range(i, n+1):
        ar[j] = min(ar[j], ar[j-i] + num)

print(ar[n])
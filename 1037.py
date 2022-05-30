import sys

input = sys.stdin.readline

ar = [[] for _ in range(1000001)]



n = int(input())
lst = list(map(int, input().split()))
lst.sort()


for i in range(2, 1000001):
    for j in range(i+i, 1000001, i):
        ar[j].append(i)
        

for i in range(2, 1000001):
    if len(ar[i]) == n and ar[i] == lst:
        print(i)
        break


# 빠른 방법
# print(max(lst)*min(lst))
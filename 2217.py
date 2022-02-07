import sys

input = sys.stdin.readline


N = int(input())

lst = []

for i in range(N):
    t = int(input())
    lst.append(t)

lst.sort(reverse = True)

for i in range(1, N):
    lst[i] = lst[i]*(i+1)

print(max(lst))

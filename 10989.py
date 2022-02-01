import sys

input = sys.stdin.readline

N = int(input())
lst=[0 for col in range(10001)]

for i in range(0, N):
    m = int(input())
    lst[m] = lst[m]+1


for i in range(1, 10001):
    k = lst[i]
    for j in range(0, k):
        print(i)
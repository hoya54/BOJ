import sys

input = sys.stdin.readline


n, k = map(int, input().split())

ar = [1]*(n+2)


for i in range(k-1):
    temp = [0]*(n+2)

    for j in range(n+1):
        temp[j] = sum(ar[:j+1])
    ar = temp[:]


print(ar[n]%1000000000)

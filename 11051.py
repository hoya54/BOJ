import sys

input = sys.stdin.readline

n, k = map(int, input().split())

ar = [0]*(n+1)
ar[1] = 1
for i in range(0, n+1):
    for j in range(i, -1, -1):
        if j == 0 or j == i:
            ar[j] = 1
        else:
            ar[j] = (ar[j-1] + ar[j])%10007
print(ar[k])


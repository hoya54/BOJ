import sys

input = sys.stdin.readline

N, X = input().split()
N = int(N)
X = int(X)

lst = list(map(int, input().split()))

for i in range(0, N):
    if lst[i] < X:
        print(lst[i], end=" ")
import sys

input = sys.stdin.readline

N = int(input())


A = map(int, input().split())
B = map(int, input().split())

A = list(A)
B = list(B)

A.sort(reverse = True)
B.sort()

r=0
for i in range(N):
    r += A[i]*B[i]
print(r)
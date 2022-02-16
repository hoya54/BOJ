import sys

input = sys.stdin.readline

N, M = map(int, input().split())

ar = list(map(int, input().split()))

summ = [0] *(N+1)
count = 0

for i in range(1, N+1):
    summ[i] = summ[i-1] + ar[i-1]

for i in range(N):
    for j in range(i+1, N+1):
        if summ[j]-summ[i] == M:
            count += 1
        elif summ[j]-summ[i] > M:
            break

print(count)

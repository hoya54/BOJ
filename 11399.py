import sys
input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))

lst = sorted(lst)

summ=0
for i in range(N, 0, -1):
    summ = summ + lst[N-i]*i
print(summ)
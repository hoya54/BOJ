import sys

input = sys.stdin.readline

T = int(input())

st = list(map(int, input().split()))

summ = 0
maxx = max(st)
for i in range(0, T):
    summ = summ + st[i]/maxx*100
print(summ/T)
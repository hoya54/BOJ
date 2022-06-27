import sys

input = sys.stdin.readline

n = int(input())

lst = []

for i in range(n):
    x, y = map(int, input().split())
    lst.append((x,y))

lst.sort()
t = []
for i in lst:
    t.append(i[1])

dp = [1]*n

for i in range(n):
    for j in range(i):
        #print(dp)
        if t[j] < t[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(n-max(dp))

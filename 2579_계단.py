import sys

input = sys.stdin.readline

N = int(input())

lst = [0]*(301)
summ = [0]*(301)

for i in range(1, N+1):
    lst[i] = int(input())


summ[1] = lst[1]
summ[2] = lst[1] + lst[2]
summ[3] = max(summ[1]+lst[3], summ[2]+lst[3])

for i in range(3, N+1):
    summ[i] = max(summ[i-3]+lst[i-1]+lst[i], summ[i-2]+lst[i])

print(summ[N])
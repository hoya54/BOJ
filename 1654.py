import sys
input = sys.stdin.readline

K, N = map(int, input().split())

lst=[]
for i in range(0, K):
    lst.append(int(input()))

mid = max(lst)
low = 1
high = mid
while low <= high:
    mid = (low+high)//2
    summ=0
    for s in lst:
        summ = summ + s//mid

    if summ >= N:
        low = mid+1
    else:
        high = mid-1

print(high)
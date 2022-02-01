import sys

input = sys.stdin.readline

N, M = input().split()

N = int(N)
M = int(M)

lst = list(map(int, input().split()))

low = 0
high = max(lst)

def check(mid, M, lst):
    summ=0
    for i in lst:
        if i-mid >0:
            summ += i-mid
        if summ >= M:
            return True
    return False

while low < high:
    mid = (low+high)//2+1   # // : 나누고 소수점 버림

    if check(mid, M, lst):
        low = mid
    else:
        high = mid-1
print(low)
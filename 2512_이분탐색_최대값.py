import sys

input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))

total = int(input())

left = 0
right = max(lst)

while left <= right:

    middle = (left+right)//2

    t = 0
    for i in lst:
        t += min(i, middle)


    if t <= total:
        left = middle+1
    else:
        right = middle -1

print(right)
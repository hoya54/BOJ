import sys

input = sys.stdin.readline

n = int(input())

bin_size = int(input())

lst = []

for i in range(n):
    lst.append(int(input()))
lst.sort()

left = 0
right = n-1

cnt = 0

while left <= right:
    if lst[left] + lst[right] <= bin_size:
        left += 1
    right -= 1
    cnt += 1

print(cnt)
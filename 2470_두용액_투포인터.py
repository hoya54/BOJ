import sys

input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))

lst.sort()

minn = sys.maxsize

start = 0
end = len(lst)-1

x = 0
y = 0

# print(lst)

while start < end:

    to_check = lst[start] + lst[end]

    if abs(to_check) < minn:
        minn = abs(to_check)
        x = lst[start]
        y = lst[end]
    
    if to_check >= 0:
        end -= 1
    else:
        start += 1

print(x, y)
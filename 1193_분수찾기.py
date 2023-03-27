import sys

input = sys.stdin.readline

line = 1
max_num = 0

n = int(input())

while n > max_num:
    max_num += line
    line += 1
 
remain = max_num - n

line -= 1

l = line
r = line

if line%2 == 0:
    l = line
    r = 1

    l -= remain
    r += remain
else:
    l = 1
    r = line

    l += remain
    r -= remain


print(l, end='/')
print(r)
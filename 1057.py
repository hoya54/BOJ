import sys

input = sys.stdin.readline

N, a, b = map(int, input().split())
count = 1

if a > b:
    tmp = a
    a = b
    b = tmp

while True:
    if a%2==1 and b%2 == 0 and a+1 == b:
        break
    if a%2 == 1:
        a = a+1
    if b%2 == 1:
        b = b+1
    a = a//2
    b = b//2
    count += 1

print(count)

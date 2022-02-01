import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

s = input().rstrip()

length = len(s)

c=2

if length <= 25:
    print(s)
else:
    for i in range(11, length - 11):
        if s[i] == ".":
            if i == 11 or i == length-12:
                continue
            c=3
            break
    if c == 2:
        print(s[0:11], end='')
        print("...", end='')
        print(s[length-11:], end='')
    else:
        print(s[0:9], end='')
        print("......", end='')
        print(s[length-10:], end='')
    
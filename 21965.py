import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))

mountain = True

inc = True

state = 1

if n >= 2:
    if lst[0] < lst[1]:
        inc = True
    else:
        inc = False


for i in range(0, n-1):
    if lst[i] == lst[i+1]:
        state = 3
        break
    
    if inc == True:
        if lst[i] < lst[i+1]:
            pass
        else:
            state += 1
            inc = False
    else:
        if lst[i] > lst[i+1]:
            pass
        else:
            state += 1
            inc = True
    
    if state >= 3:
        break

if state == 1 or state == 2:
    print("YES")
else:
    print("NO")



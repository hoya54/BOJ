import sys
from itertools import combinations
from collections import deque


N = int(input())

st = input()
state = 0
for i in range(N):
    if st[i] == 'A' or st[i] == 'V' or st[i] == 'J':
        continue
    else:
        print(st[i], end='')
        state=1

if state == 0:
    print("nojava")
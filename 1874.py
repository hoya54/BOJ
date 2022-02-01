import sys
input = sys.stdin.readline

N = int(input())

from collections import deque
i=0
s = deque()

state=1
result=[]
inp = []

for j in range(1, N+1):
    inp.append(int(input()))

for j in range(0, N):
    a = inp[j]
    if a > i: 
        while a != i:
            i += 1
            s.append(i)
            result.append("+")
    if a==s[-1]:
        s.pop()
        result.append("-")
    else:
        break

if len(s)!= 0:
    print("NO")
else:
    for i in range(0, 2*N):
        print("{0}".format(result[i]))

import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

def func(a, b):
    d = deque()
    visited=[0]*10000
    d.append([a, ""])
    visited[a]=1

    while d:
        num, path = d.popleft()
        
        if num == b:
            return path

        x1 = (num*2)%10000
        if visited[x1] == 0:
            visited[x1] = 1
            d.append([x1, path+"D"])

        x2=0
        if num == 0:
            x2 = 9999
        else:
            x2 = num-1
        if visited[x2] == 0:
            visited[x2] = 1
            d.append([x2, path+"S"])


        x3 = (num%1000)*10 + num//1000
        if visited[x3] == 0:
            visited[x3] = 1
            d.append([x3, path+"L"])

        x4 = num//10 + num%10*1000
        if visited[x4] == 0:
            visited[x4] = 1
            d.append([x4, path+"R"])



for i in range(0, T):
    a, b = map(int, input().split())
    

    r = func(a, b)
    print(r)
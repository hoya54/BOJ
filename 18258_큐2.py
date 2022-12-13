import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

d = deque()

for i in range(n): 
    lst = input().split()

    print(type(lst))
    
    if(lst[0] == "push"):
        d.append(int(lst[1]))
    elif(lst[0] == "pop"):
        if(len(d) == 0):
            print(-1)
        else:
            print(d.popleft())
    elif(lst[0] == "size"):
        print(len(d))
    elif(lst[0] == "empty"):
        if(len(d) == 0):
            print(1)
        else:
            print(0)
    elif(lst[0] == "front"):
        if(len(d) == 0):
            print(-1)
        else:
            print(d[0])
    elif(lst[0] == "back"):
        if(len(d) == 0):
            print(-1)
        else:
            print(d[-1])
    

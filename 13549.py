import sys

from collections import deque

input = sys.stdin.readline

n, t = map(int, input().split())

visited=[0]*100002

def func():
    global visited

    d = deque()
    d.append(n)
    visited[n] = 1
    s = n

    while s <= 100000 and s != 0:
        if visited[s]==0:
            d.append(s)
            #visited[s]=1
        s = s*2

    cnt =0
    
    while d:
        end = len(d)

        for i in range(end):
            #print(d)
            temp = d.popleft()
            #print(temp)
            if temp == t:
                print(cnt)
                return

            if visited[temp+1] == 0 and temp+1 <= t:
                d.append(temp+1)
                visited[temp+1]=1

                s = temp+1

                while s <= 100000 and s != 0:
                    if visited[s]==0:
                        d.append(s)
                    s = s*2
                    

            if visited[temp-1] == 0 and temp-1 >= 0:
                d.append(temp-1)
                visited[temp-1]=1

                s = temp-1

                while s <= 100000 and s != 0:
                    if visited[s]==0:
                        d.append(s)
                    s = s*2
        cnt += 1

func()
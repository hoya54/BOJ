import sys
from collections import deque

input = sys.stdin.readline

A, B = map(int, input().split())


cnt=0
state = 0

# BFS 사용
def func():
    global state
    global cnt

    d =deque()

    d.append(A)

    while d:
        end = len(d)

        for i in range(0, end):
            t = d.popleft()

            if t == B:
                state=1
                return
            else:
                if t*2 <= B:
                    d.append(t*2)
                if t*10+1 <= B:
                    d.append(t*10+1)

        cnt += 1

#B를 A로 가면서 확인
def func2():
    t = B
    c=0

    while True:
    
        if t == A:
            print(c+1)
            return
        elif t%2 == 0:
            t = t//2
        elif t%10 == 1:
            t = t//10
        else:
            print(-1)
            return

        if t < A:
            print(-1)
            return
        c += 1

func()
if state==1:
    print(cnt+1)
else:
    print(-1)
func2()
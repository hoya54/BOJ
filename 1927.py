import sys
import heapq
input = sys.stdin.readline

N = int(input())
h=[]


for i in range(0, N):
    a = int(input())
    if a==0:
        if len(h)==0:
            print(0)
        else:
            print(heapq.heappop(h))
    else:
        heapq.heappush(h, a)
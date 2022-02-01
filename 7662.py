import sys
import heapq
input = sys.stdin.readline

T = int(input())



for i in range(0, T):
    n = int(input())
    cnt=0
    max_h=[]
    min_h=[]
    dic={}
    result=[]
    for j in range(0, n):
        a, b = input().split()
        
        b = int(b)
        

        if a =='I':
            heapq.heappush(max_h, (-b, b))
            heapq.heappush(min_h, b)
            cnt += 1
            if b in dic:
                dic[b] = dic[b]+1
            else:
                dic[b] = 1
        else:
            if cnt==0:
                continue
            
            if b==1:
                while True:
                    t = heapq.heappop(max_h)[1]
                    if t in dic:
                        dic[t] = dic[t]-1
                        if dic[t]==0:
                            del dic[t]
                        break
            else:
                while True:
                    t = heapq.heappop(min_h)

                    if t in dic:
                        dic[t] = dic[t]-1
                        if dic[t]==0:
                            del dic[t]
                        break
            cnt -= 1
    if cnt==0:
        print("EMPTY")
    else:
        if cnt==1:
            while True:
                t = heapq.heappop(max_h)[1]
                if t in dic:
                    print(t, t)
                    break

        else:
            while True:
                t = heapq.heappop(max_h)[1]
                if t in dic:
                    print(t, end=" ")
                    break

            while True:
                t = heapq.heappop(min_h)
                if t in dic:
                    print(t)
                    break
                        
                

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
            print(heapq.heappop(h)[1])
    else:
        heapq.heappush(h, (-a, a))


# 라이브러리 미사용 버전 
# def insert(a):
#     global h

#     if len(h)==0:
#         h.append(a)
#     else:
#         ind = len(h)
#         if h[0] > a:
#             h.append(a)

#             while True:
#                 p = (ind-1)//2
#                 if p == 0:
#                     break
#                 if h[ind] > h[p]:
#                     temp = h[ind]
#                     h[ind] = h[p]
#                     h[p] = temp
#                 else:
#                     break
#                 ind = p

#         else:
#             origin = h[0]
#             h[0] = a
#             h.append(origin)

#             while True:
#                 p = (ind-1)//2
#                 if p == 0:
#                     break
#                 if h[ind] > h[p]:
#                     temp = h[ind]
#                     h[ind] = h[p]
#                     h[p] = temp
#                 else:
#                     break
#                 ind = p

# def pop():
#     if len(h)==0:
#         return 0

#     r = h[0]

#     h[0] = h[len(h)-1]
#     h.pop()

#     ind=0

#     while True:

#         #왼쪽 자식만
#         left = ind*2+1
#         right = ind*2+2

#         if left < len(h) and right == len(h) :
#             if h[left] > h[ind]:
#                 temp = h[left]
#                 h[left] = h[ind]
#                 h[ind] = temp
#                 ind = left
#         elif right <=len(h):
#             if h[left] > h[right]:
#                 target = left
#             else:
#                 target = right
#             temp = h[target]
#             h[target] = h[ind]
#             h[ind] = temp
#             ind = target
#         else:
#             break 
#     return r
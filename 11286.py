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
        heapq.heappush(h, (abs(-a), a))

#for i in range(0, len(result)):
    #print(result[i])


# 힙 두개 사용

#양수 전용 힙(original)
# h_min=[]

# #음수 전용 힙
# h_max=[]

# result=[]
# for i in range(0, N):
#     a = int(input())
#     if a==0:
#         if len(h_max)==0 and len(h_min)!=0:
#             result.append(heapq.heappop(h_min))
#         elif len(h_max)!=0 and len(h_min)==0:
#             result.append(heapq.heappop(h_max)[1])
#         elif len(h_max)==0 and len(h_min)==0:
#             result.append(0)
#         else:
#             plus = heapq.heappop(h_min)
#             minus = heapq.heappop(h_max)[1]

#             if plus == (-1)*minus:
#                 result.append(minus)
#                 heapq.heappush(h_min, plus)
#             elif (-1)*minus < plus:
#                 result.append(minus)
#                 heapq.heappush(h_min, plus)
#             else:
#                 result.append(plus)
#                 heapq.heappush(h_max, (-minus, minus))

#     elif a < 0:
#         heapq.heappush(h_max, (-a, a))
#     else:
#         heapq.heappush(h_min, a)
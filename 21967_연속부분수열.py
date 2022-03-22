import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))

d = deque()


answer = 0
ar = [0]*11

def max_minus_min():
    minn = 0
    for i in range(1, 11):
        if ar[i] > 0:
            minn = i
            break

    maxx = 0
    for i in range(10, 0, -1):
        if ar[i] > 0:
            maxx = i
            break
    
    return maxx-minn

for i in range(0, n):
    ar[lst[i]] += 1
    d.append(lst[i])

    while d and max_minus_min() > 2:
        out = d.popleft()
        ar[out] -= 1
        
    answer = max(answer, len(d))

print(answer)




# import sys

# input = sys.stdin.readline

# n = int(input())
# A = list(map(int, input().split()))


# max = 0
# for i in range(1, 9):
#     cnt=0
#     for j in A:
#         if i <= j <= i+2:
#             cnt += 1
#             if cnt > max:
#                 max = cnt
#         else:
#             cnt = 0
# print(max)   
#모든 번호에 대해 누를 수 있는지 확인하는 방법 (더 느리지만 예외처리 필요없음)

import sys

input = sys.stdin.readline

N = int(input())

M = int(input())
nums=[]

if M >0:
    nums = list(map(str, input().split()))

def possible_num(x):

    x = list(str(x))
    for element in x:
        if element in nums:
            return False
    return True

answer = abs(N - 100)

for temp in range(1000001):
    if possible_num(temp) is True:
        answer = min(answer, len(str(temp)) + abs(N-temp))
print(answer)



# import sys

# sys.setrecursionlimit(1000000)

# input = sys.stdin.readline

# T = int(input())

# minn = 999999999
# a = 0
# count = 9999999999

# def func(cur,  nums, cnt):
#     global minn
#     global a
#     global count
#     global T

#     cnt += 1
#     #print(cur)
#     if abs(T-cur) < minn:
#         minn = abs(T-cur)
#         #if count > cnt:
#         count = cnt
#         if minn == 0:
#             a=1
#             return
#     elif abs(T-cur) == minn:
#         if count > cnt:
#             count = cnt
    
#     if cur != 0:
#         for i in nums:
            
#             if cur*10+i - T < minn:
#                 #print(cur*10+i)
#                 func(cur*10+i, nums, cnt)

    

# n = int(input())
# nums=[]
# if n >0:
#     temp = list(map(int, input().split()))

#     for i in range(0, 10):
#         if i not in temp:
#             nums.append(i)
# else:
#     nums = [0,1,2,3,4,5,6,7,8,9]

# for i in nums:
#     func(i, nums, 0)

# if a==1:
#     print(min(count, abs(100-T)))
# else:
#     print(min(minn+count, abs(100-T)))



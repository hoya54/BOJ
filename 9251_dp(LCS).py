import sys

input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()

la = len(A)
lb = len(B)

# 2차원 배열 사용
ar = [[0 for _ in range(la+1)] for _ in range(lb+1)]

for i in range(1, lb+1):
    for j in range(1, la+1):
        if A[j-1] == B[i-1]:
            ar[i][j] = ar[i-1][j-1] + 1
        else:
            ar[i][j] = max(ar[i-1][j], ar[i][j-1])

print(ar[lb][la])


# 1차원 배열 사용
# ar2 = [0 for _ in range(la+1)]

# for i in range(1, lb+1):
#     t = 0
#     for j in range(1, la+1):
#         if t < ar2[j]:
#             t = ar2[j]
#         elif A[j-1] == B[i-1]:
#             ar2[j] = t + 1
#     #print(ar2)
# print(max(ar2))



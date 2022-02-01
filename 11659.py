import sys

input = sys.stdin.readline

N, M = map(int, input().split())

lst=[]

lst = list(map(int, input().split()))
sum_lst = []
sum_lst.append(lst[0])
for i in range(1, len(lst)):
    sum_lst.append(sum_lst[i-1]+lst[i])
result=[]

for i in range(0, M):
    a, b = map(int, input().split())
    if a==1:
        result.append(sum_lst[b-1])
    else:
        result.append(sum_lst[b-1]-sum_lst[a-2])

for i in range(0, M):
    print(result[i])
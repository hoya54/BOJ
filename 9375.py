import sys

input = sys.stdin.readline

T = int(input())


result=[]
for i in range(0, T):
    n = int(input())
    lst={}
    for j in range(0, n):
        a, b = map(str, input().split())

        if b in lst.keys():
            lst[b].append(a)
        else:
            lst[b]=[a,""] # ""는 사용하지 않는 경우를 카운트 하기 위해 사용

    ans = 1
    for k in lst.keys():
        ans *= len(lst[k])
    result.append(ans-1)

for i in range(0, T):
    print(result[i])

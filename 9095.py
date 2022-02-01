import sys
input = sys.stdin.readline

T = int(input())
summ=[0] *(11)
summ[1]=1
summ[2]=2
summ[3]=4

cnt = 0

def func(n):
    global summ
    global cnt

    if summ[n] != 0:
        return summ[n]

    if n-3 > 0:
        cnt = cnt + func(n-3)
    if n-2 > 0:
        cnt = cnt + func(n-2)
    if n-1 > 0:
        cnt = cnt + func(n-1)
    return cnt
    

for i in range(1, 11):
    cnt = 0
    summ[i] = func(i)

result = []
for i in range(0, T):
    n = int(input())
    result.append(summ[n])

for i in range(0, T):   
    print(result[i])
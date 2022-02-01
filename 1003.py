import sys
input = sys.stdin.readline

summ = [0]*41
lst0=[0]*41
lst1=[0]*41
inp=[]

#시간초과로 피보나찌 재귀함수는 사용불가
def fibonacci(n):
    global lst0
    global lst1
    if lst0[n] == 0 and lst1[n]==0:
        return summ[n]
    else:
        if n==0:
            lst0[0] += 1
            return 0
        elif n==1:
            lst1[1] += 1
            return 1
        else:
            return fibonacci(n-1)+fibonacci(n-2)


T = int(input())

for i in range(0, T):
    n = int(input())
    inp.append(n)
maxx = max(inp) # 최댓값만큼만 반복

lst0[0]=1

lst1[1]=1

for i in range(2, maxx+1):
    lst0[i] = lst0[i-1]+lst0[i-2]
    lst1[i] = lst1[i-1]+lst1[i-2]
for i in range(0, T):
    print(lst0[inp[i]], lst1[inp[i]])
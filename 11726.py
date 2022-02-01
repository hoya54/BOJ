import sys

input = sys.stdin.readline

n = int(input())

summ=[0]*(n+1)

summ[1]=1

if n>=2:
    summ[2]=2



for i in range(3, n+1):
    summ[i] = summ[i-2]+summ[i-1]

print(summ[n]%10007)
        
import sys
import math
input = sys.stdin.readline

M ,N = input().split()
N = int(N)
M= int(M)

def func(a, b):
    lst=[]
    for i in range(0, b+1):
        lst.append(1)
    lst[1]=0
    lst[0]=0
    i=2
    while True:
        if i*i > b:
            break
        if lst[i] == 1:
            for j in range(i*i, b+1, i):
                lst[j]=0
        i = i+1

    for i in range(a, b+1):
        if lst[i]==1:
            print(i)

func(M, N)
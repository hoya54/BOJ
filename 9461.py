import sys

input = sys.stdin.readline

T = int(input())

summ=[0,1,1,1,2,2]

for i in range(6, 101):
    summ.append(summ[i-5]+summ[i-1])

for i in range(0, T):
    print(summ[int(input())])
import sys
input = sys.stdin.readline

N = int(input())

st = input()

summ=0
for i in range(0, N):
    c = ord(st[i])-96
    summ = summ + c*31**i
print(summ%1234567891)
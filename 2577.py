import sys

input = sys.stdin.readline

a= int(input())
b= int(input())
c= int(input())

s = a*b*c
s = str(s)

for i in range(0, 10):
    print(s.count(str(i)))
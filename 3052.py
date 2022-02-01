import sys

input = sys.stdin.readline

lst=[]
for i in range(0, 10):
    a = int(input())
    n = a%42
    if n not in lst:
        lst.append(n)

print(len(lst))
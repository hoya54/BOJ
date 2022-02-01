import sys
input = sys.stdin.readline

N = int(input())

lst=[]
count=0
for i in range(0, N):
    a = int(input())
    if a == 0:
        lst.pop()
        count -= 1
    else:
        lst.append(a)
        count += 1
sum=0
for i in range(0, count):
    sum = sum + lst[i]
print(sum)
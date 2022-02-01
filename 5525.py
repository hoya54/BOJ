import sys

input = sys.stdin.readline

N = int(input())

length = int(input())

st = input().rstrip()

cnt=0
i=1
l=0

while i<length-1:
    if st[i-1]=='I' and st[i]=='O' and st[i+1]=='I':
        l += 1
        if l == N:
            l -= 1
            cnt += 1
        i +=1
    else:
        l=0
    i += 1
print(cnt)
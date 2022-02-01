import sys

input = sys.stdin.readline

N = int(input())
lst=[]

lst = list(map(int, input().split()))
s = set(lst)
s = list(s)
s.sort()
#print(s)

r = []
d= {}
for i in range(len(s)):
    temp = s[i]
    d[temp] = i

for i in range(0, N):
    print(d[lst[i]], end=" ")
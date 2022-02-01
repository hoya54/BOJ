import sys

input = sys.stdin.readline

st = input().upper()
lst=[0 for i in range(26)]

for i in range(0, len(st)-1):
    c = ord(st[i])-65
    lst[c] += 1

maxx = max(lst)
inn = lst.index(max(lst))
lst[inn]=0

if maxx not in lst:
    print(chr(inn+65))
else:
    print("?")
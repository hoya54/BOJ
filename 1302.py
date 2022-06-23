import sys

input = sys.stdin.readline

n = int(input())

dic = {}

for i in range(n):
    st = input().rstrip()

    if st not in dic:
        dic[st] = 1
    else:
        dic[st] += 1

maxx = max(dic.values())


lst = []
for k, v in dic.items():
    if v == maxx:
        lst.append(k)

lst.sort()

print(lst[0])





    



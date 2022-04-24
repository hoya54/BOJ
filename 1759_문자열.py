import sys
from itertools import combinations

input = sys.stdin.readline

L, C = map(int, input().split())

lst = list(map(str, input().split()))

lst.sort()
ar = [0]*26
aeiou = []
remainder = []

for i in range(C):
    index = ord(lst[i]) - 96
    if index == 1 or index == 5 or index == 9 or index == 15 or index == 21:
        aeiou.append(index)
    else:
        remainder.append(index)

result = []

for i in range(1, len(aeiou)+1):
    if i+2 > L:
        continue

    bench = []

    r = []
    for j in combinations(aeiou, i):
        bench.append(list(j))
    
    for j in combinations(remainder, L-i):
        for k in bench:
            r.append(k + list(j))
    for j in range(len(r)):
        t = r[j]
        t.sort()
        result.append(t)

r = []

for t in result:
    st = ""
    for k in range(L):
        st += chr(t[k]+96)
    r.append(st)

r = sorted(r)
for i in r:
    print(i)


    


import sys
import heapq


input = sys.stdin.readline

N, M = map(int, input().split())

ar = [[0 for _ in range(N)] for _ in range(N)]

house = 0
bbq = 0

h = []
b = []

for i in range(N):
    st = list(map(int, input().split()))
    for j in range(N):
        ar[i][j] = st[j]
        if st[j] == 1:
            house += 1
            h.append((i, j))
        elif st[j] == 2:
            bbq += 1
            b.append((i, j))

include = [0]*bbq
lst = [[0 for _ in range(bbq)] for _ in range(house)]



for i in range(house):
    for j in range(bbq):
        lst[i][j] = abs(h[i][0] - b[j][0]) + abs(h[i][1] - b[j][1])


def func(t):
    summ = 0
    for i in range(house):
        minn = 10000

        for j in range(len(lst[0])):
            if j == t:
                continue
            else:
                if minn > lst[i][j]:
                    minn = lst[i][j]
        
        summ += minn
    
    return summ

print(lst)


for t in range(bbq-M):
    tmp = []
    for i in range(len(lst[0])):
        tmp.append(func(i))
    
    target = tmp.index(min(tmp))
    #print(target)
    #print(lst)
    for i in range(house):
        del lst[i][target]
    #print(lst)

summ=0
for i in range(house):
    summ += min(lst[i])

print(summ)



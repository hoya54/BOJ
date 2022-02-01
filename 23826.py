import sys
import itertools 

input = sys.stdin.readline

N = int(input())

lst = []
dic = {}

hx, hy, he = map(int, input().split())
if N==1:
    x, y, e = map(int, input().split())
    t = max(0, he - (abs(x-hx)+abs(y-hy))-e)
    if t == 0:
        print('IMPOSSIBLE')
    else:
        print(t)
    
else:

    for i in range(1, N+1):
        x, y, e = map(int, input().split())
        lst.append((x, y, e))
        dic[x,y] = e

    for i in itertools.combinations(lst, 2):
        a = i[0][0]
        b = i[0][1]
        p = i[0][2]

        c = i[1][0]
        d = i[1][1]
        q = i[1][2]

        dic[a, b] += max(0, q - (abs(a-c)+abs(b-d)))
        dic[c, d] += max(0, p - (abs(a-c)+abs(b-d)))


    maxx = 0
    for i in lst:
        a = i[0]
        b = i[1]

        temp = he - (abs(a-hx)+abs(b-hy)) - dic[a,b]
        t = max(0, temp)
        if t > maxx:
            maxx = t

    if maxx == 0:
        print('IMPOSSIBLE')
    else:
        print(maxx)
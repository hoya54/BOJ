from itertools import combinations
import math
import sys

input = sys.stdin.readline

t = int(input())

for k in range(t):
    
    n = int(input())

    lst = []
    for i in range(n):
        x, y = map(int, input().split())
        lst.append((x, y))
    
    

    minn = math.inf

    for i in combinations(lst, n//2):
        fromm = list(i)
        temp = []

        for j in lst:
            if j not in fromm:
                temp.append(j)
        
        for to in combinations(temp, n//2):
            to = list(to)
            
            x = 0
            y = 0

            for j in range(n//2):
                x1 = fromm[j][0]
                y1 = fromm[j][1]

                x2 = to[j][0]
                y2 = to[j][1]


                tx = x2-x1
                ty = y2-y1
                #print(x1, y1, x2, y2, tx, ty)
                x += tx
                y += ty

            vector = math.sqrt(x**2 + y**2)
            minn = min(minn, vector)


    print(minn)

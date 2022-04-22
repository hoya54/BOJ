import sys
import math

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())

    d = y-x

    if d == 1:
        print(1)
    elif d == 2:
        print(2)
    elif d == 3:
        print(3)
    else:
        low = math.floor(math.sqrt(d))
        if low**2 == d:
            print(2*low-1)
        else:
            if low**2 < d <= low**2 + low:
                print(2*low-1 + 1)
            else:
                print(2*low-1 + 2)


    


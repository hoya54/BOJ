import sys
input = sys.stdin.readline

N = int(input())

g = 6
distance = 2
i=1

state = 1
if N==1:
    print(1)
elif 2<=N<=7:
    print(2)
else:
    while True:
        i = i+g
        if N <= i:
            break
        else:
            distance = distance+1
            g = g+6
    print(distance)
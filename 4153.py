import sys
input = sys.stdin.readline

while True:
    lst = list(map(int, input().split()))

    lst.sort()

    z = lst.pop()
    y = lst.pop()
    x = lst.pop()

    if x==0 and y==0 and z==0:
        break

    if z*z == x*x+y*y:
        print("right")
    else:
        print("wrong")
    
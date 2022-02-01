import sys

input = sys.stdin.readline

T = int(input())

def func(a, b):
    if a < b:
        temp = a
        a = b
        b = temp
    while b!=0:
        r = a%b
        a = b
        b = r
    return a


for i in range(0, T):
    M, N, x, y = map(int, input().split())

    cnt = 1
    r = func(M, N)
    r = M*N/r
    a= x
    b = y
    
    while True:
        if a == b:
            print(a)
            break
        elif a > b:
            b += N
        else:
            a += M
        if a > r and b>r:
            print(-1)
            break


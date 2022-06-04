import sys

input = sys.stdin.readline

t = int(input())

prime = [1]*1001
p = []

for i in range(2, 1001):
    if prime[i] == 1:
        p.append(i)
        for j in range(i+i, 1001, i):
            prime[j] = 0

for _ in range(t):
    n = int(input())

    r = 0
    x = 0
    y = 0
    for i in p:
        for j in p:
            for k in p:
                if i+j+k == n:
                    r, x, y = i, j, k
                    break
            if r != 0:
                break
        if r != 0:
            break
    if r == 0:
        print(0)
    else:
        print(r, x, y)

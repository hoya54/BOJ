import sys
input = sys.stdin.readline

N = int(input())

prime = [-1]*6000

for i in range(2, 6000):
    if prime[i] == -1:
        prime[i] = 1
        for j in range(i+i, 6000, i):
            prime[j] = 0

for i in range(N):
    n = int(input())

    a = n//2
    b = n//2

    while True:
        if prime[a] and prime[b]:
            print(a, b)
            break
        else:
            a -= 1
            b += 1
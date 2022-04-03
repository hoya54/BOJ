import sys

input = sys.stdin.readline

prime = [1] * 1000001

for i in range(2, 1000001):
    if prime[i] == 1:
        for j in range(i+i, 1000001, i):
            prime[j] = 0



while True:
    n = int(input())
    if n == 0:
        break
    
    a, b = 0, 0
    for i in range(3, n//2+1, 2):
        if prime[i] == 1 and prime[n-i] == 1:
            a = i
            b = n-i
            break
    
    if a != 0:
        print("{} = {} + {}".format(n, a, b))
    else:
        print("Goldbach's conjecture is wrong.")


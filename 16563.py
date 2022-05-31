import sys

input = sys.stdin.readline

ar = [i for i in range(5000001)]


for i in range(2, 5000001):
    if ar[i] == i:
        for j in range(i*i, 5000001, i):
            if ar[j] == j:
                ar[j] = i

t = int(input())

lst = list(map(int, input().split()))

for n in lst:
    r = []

    while n > 1:
        r.append(ar[n])
        n = n//ar[n]

    print(' '.join(map(str, r)))

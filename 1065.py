import sys

input = sys.stdin.readline


N = int(input())

count = 0

if N <= 99:
    count = N
else:
    count = 99

    for i in range(100, N+1):
        t = i

        a = t//100
        t = t%100

        b = t//10

        c = t%10

        if b-a == c-b:
            count += 1


print(count)
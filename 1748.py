import sys

input = sys.stdin.readline

N = int(input())

last = 0
limit = 10
i = 1
series9 = 9

count = 0
while True:
    if N >= limit:
        count += series9*i
    else:
        break
    limit = limit * 10
    series9 = series9*10
    i += 1

last = limit//10

print((N - last + 1)*i + count)
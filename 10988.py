st = list(input())

r = list(st[:])
r.reverse()

if r == st:
    print(1)
else:
    print(0)
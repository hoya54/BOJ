n = int(input())

for i in range(0, n):
    m, st = input().split()
    m = int(m)
    length = len(st)
    for j in range(0, length):
        for k in range(0, m):
            print("{0}".format(st[j]), end="")
    print()
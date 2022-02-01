import sys
input = sys.stdin.readline

N = int(input())
lst = []

for i in range(0, N):
    x, y = input().split()
    x = int(x)
    y = int(y)
    lst.append([x, y])

from operator import itemgetter
lst.sort(key=itemgetter(1))
lst.sort(key=itemgetter(0))

for i in range(0, N):
    print("{0} {1}".format(lst[i][0], lst[i][1]))

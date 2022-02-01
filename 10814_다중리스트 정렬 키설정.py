N = int(input())
lst=[]

for i in range(0, N):
    a, b = input().split()
    a = int(a)
    lst.append([a, b])
from operator import itemgetter
lst.sort(key=itemgetter(0))

for i in range(0, N):
    print("{0} {1}".format(str(lst[i][0]), str(lst[i][1])))
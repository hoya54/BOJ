import sys
input = sys.stdin.readline

N = int(input())
lst1 = list(map(int, input().split()))

M = int(input())
lst2 = list(map(int, input().split()))

from collections import Counter
cn = Counter(lst1)
for i in range(0, M):
    print("{0} ".format(cn[lst2[i]]), end="")
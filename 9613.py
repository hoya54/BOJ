import sys
import math
from itertools import combinations

input = sys.stdin.readline


T = int(input())

for i in range(T):
    lst = list(map(int, input().split()))
    count = 0
    del lst[0]
    for j in combinations(lst, 2):
        a = int(j[0])
        b = int(j[1])
        count += math.gcd(a, b)
    print(count)
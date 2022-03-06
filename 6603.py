import sys
from itertools import combinations

input = sys.stdin.readline

while True:
    lst = list(map(int, input().split()))

    if lst[0] == 0:
        break
    
    for i in combinations(lst[1:], 6):
        print(' '.join(map(str, i)))
    print()
    


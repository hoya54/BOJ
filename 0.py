import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline


N = int(input())
a = list(map(int, input().split()))

M = int(input())
b = list(map(int, input().split()))

a.sort()

def binary_search(lst, start, end, target):
    if start > end:
        return 0
    
    mid = (start+end)//2

    if lst[mid] == target:
        return 1
    elif lst[mid] > target:
        end = mid-1
    else:
        start = mid+1

    return binary_search(lst, start, end, target)


for i in b:
    r = binary_search(a, 0, len(a)-1, i)
    print(r, end=" ")

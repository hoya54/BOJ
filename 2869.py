import sys

input = sys.stdin.readline

A, B, V = input().split()
A=int(A)
B=int(B)
V=int(V)
day=0
one_day = A-B
dest = V-B
import math
print(math.ceil(dest/one_day))
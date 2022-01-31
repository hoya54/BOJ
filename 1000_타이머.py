import sys

input = sys.stdin.readline

A, B = input().split()
print(int(A)+int(B))

import time
start = time.time()
print("time :", time.time() - start)
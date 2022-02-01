import sys


input = sys.stdin.readline

N, M = map(int, input().split())

t = min(N, M)
t = t//2
print(t)

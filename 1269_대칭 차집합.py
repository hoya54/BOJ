import sys


input = sys.stdin.readline


n, m = map(int, input().split())

a = map(int, input().split())
a = set(a)

b = map(int, input().split())
b = set(b)


print(len((a-b).union((b-a))))
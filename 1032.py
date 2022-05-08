import sys

input = sys.stdin.readline

n = int(input())

lst = list(input().rstrip())

for _ in range(n-1):
    st = input().rstrip()
    for i in range(len(lst)):
        if lst[i] != st[i]:
            lst[i] = '?'

print(''.join(lst))
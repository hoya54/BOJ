import sys

input = sys.stdin.readline

st = list(map(int, input().split()))

print((st[0]**2+st[1]**2+st[2]**2+st[3]**2+st[4]**2)%10)
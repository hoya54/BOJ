import sys
import math

input = sys.stdin.readline

x, y = map(int, input().split())
a, b = map(int, input().split())

up = x*b + y*a
down = y*b

rem = math.gcd(up, down)

up //= rem
down //= rem
print(up, down)
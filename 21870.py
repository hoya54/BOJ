import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

s=[]

s = list(map(int, input().split()))

def multi_gcd(lst):

    result = lst[0]

    for i in range(1, len(lst)):
        a = result
        b = lst[i]
        while b !=0:
            r = a%b
            a=b
            b=r
        result = a
    return result

maxx = 0

def func(lst, summ):
    global maxx

    left = len(lst)//2

    if len(lst) == 1:
        if maxx < summ + lst[0]:
            maxx = summ + lst[0]
    else:   
        func(lst[:left], summ + multi_gcd(lst[left:]))
        func(lst[left:], summ + multi_gcd(lst[:left]))

func(s, 0)
print(maxx)
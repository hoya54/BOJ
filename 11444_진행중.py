import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())

n1 = 0
n2 = 1
r = 0
for i in range(2, N+1):

    r = n1+n2

    n1 = n2
    n2 = r
    
if N==1:
    print(0)
elif N == 2:
    print(1)
else:
    print(r%1000000007)
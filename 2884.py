import sys

input = sys.stdin.readline

H, M = input().split()

H=int(H)
M=int(M)

M = M-45

if M<0:
    M = M + 60
    H = H-1
if H<0:
    H = H+24

print(H, M)
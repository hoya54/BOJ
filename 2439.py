import sys
input = sys.stdin.readline

N = int(input())

for i in range(0, N):
    for j in range(1, N-i):
        print(" ", end="")
    for j in range(0, i+1):
        print("*", end="")
    print()
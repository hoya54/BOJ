import sys
input = sys.stdin.readline

T = int(input())

for i in range(0, T):
    H, W, N = input().split()
    H=int(H)
    W=int(W)
    N=int(N)

    p=0
    for j in range(0, W):
        for k in range(0, H):
            p += 1
            if p == N:
                print("%d%02d" % (k+1, j+1))
                
    
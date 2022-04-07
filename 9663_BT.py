import sys

input = sys.stdin.readline

N = int(input())

ans = 0

def available(ar, x, depth):
    if ar[x] != 0:
        return False
    else:
        for i in range(1, depth):
            if x-i >= 1 and ar[x-i] == depth - i:
                return False
            if x+i <= N and ar[x+i] == depth - i:
                return False
    return True

def DFS(ar, depth):
    global ans
    
    if depth == N+1:
        ans += 1
    else:
        for i in range(1, N+1):
            if available(ar, i, depth):
                ar[i] = depth
                DFS(ar, i, depth+1)
                ar[i] = 0

ar = [0]*(N+1)
DFS(ar, 1)

print(ans)
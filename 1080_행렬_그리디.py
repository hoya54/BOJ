import sys

input = sys.stdin.readline

n, m = map(int, input().split())

A = [[0 for _ in range(m)] for _ in range(n)]
B = [[0 for _ in range(m)] for _ in range(n)]


for i in range(n):
    st = input()

    for j in range(m):
        A[i][j] = int(st[j])

for i in range(n):
    st = input()

    for j in range(m):
        B[i][j] = int(st[j])

def turn(x, y):
    global A

    for i in range(3):
        for j in range(3):
            A[x+i][y+j] = (A[x+i][y+j] + 1) %2

count = 0
for i in range(n-2):
    for j in range(m-2):
        if(A[i][j] != B[i][j]):
            turn(i, j)
            count += 1

is_same = True

for i in range(n):
    for j in range(m):
        if(A[i][j] != B[i][j]):
            is_same = False
            break

if(is_same):
    print(count)
else:
    print(-1)

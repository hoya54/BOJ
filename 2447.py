import sys

input = sys.stdin.readline


N = int(input())

ar = [[' ' for i in range(N)] for j in range(N)]


def func(n, x, y):
    if n == 3:
        ar[x][y] = '*'
        ar[x][y+1] = '*'
        ar[x][y+2] = '*'
        ar[x+1][y] = '*'
        ar[x+1][y+2] = '*'
        ar[x+2][y] = '*'
        ar[x+2][y+1] = '*'
        ar[x+2][y+2] = '*'
        return

    n = n//3

    func(n, x, y)
    func(n, x, y+n)
    func(n, x, y+2*n)

    func(n, x+n, y)
    func(n, x+n, y+2*n)

    func(n, x+2*n, y)
    func(n, x+2*n, y+n)
    func(n, x+2*n, y+2*n)


func(N, 0, 0)

for i in range(N):
    print(''.join(map(str, ar[i])))
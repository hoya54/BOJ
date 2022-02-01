import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())

lst=[]

for i in range(0, N):
    st = list(map(int, input().split()))
    lst.append(st)

summ=0

for i in range(1, N):
    for j in range(0, i+1):

        if j == 0:
            lst[i][j] = lst[i-1][j] + lst[i][j]
        elif j == i:
            lst[i][j] = lst[i-1][j-1] + lst[i][j]
        else:
            lst[i][j] = lst[i][j] + max(lst[i-1][j-1], lst[i-1][j])

print(max(lst[N-1]))

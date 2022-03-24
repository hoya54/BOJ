import sys


N = int(input())

lst = list(map(int, input().split()))

plus, minus, multi, di = map(int, input().split())

minn = 10000000000
maxx = -10000000000


def dfs(n, idx, pl, mi, ml, div):
    global maxx
    global minn

    if idx == N:
        maxx = max(maxx, n)
        minn = min(minn, n)
    
    if pl > 0:
        dfs(n + lst[idx], idx+1, pl-1, mi, ml, div)
    if mi > 0:
        dfs(n - lst[idx], idx+1, pl, mi-1, ml, div)
    if ml > 0:
        dfs(n * lst[idx], idx+1, pl, mi, ml-1, div)
    if div > 0:
        dfs(int(n / lst[idx]), idx+1, pl, mi, ml, div-1)


dfs(lst[0], 1, plus, minus, multi, di)

print(maxx)
print(minn)
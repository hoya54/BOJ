import sys

N = int(input())

lst = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    temp = input().rstrip()
    for j in range(N):
        lst[i][j] = temp[j]

maxx = 1

def func(ar, N):
    large = 1
    for i in range(N):
        t = 1
        for j in range(1, N):
            if ar[i][j-1] == ar[i][j]:
                t += 1
                if t > large:
                    large = t
            else:
                t = 1
        t=1
        for j in range(1, N):
            if ar[j-1][i] == ar[j][i]:
                t += 1
                if t > large:
                    large = t
            else:
                t = 1

    return large


for i in range(N):
    for j in range(N):
        if i == j:
            continue
        else:
            if j+1 < N and lst[i][j] != lst[i][j+1]:
                tmp = lst[i][j]
                lst[i][j] = lst[i][j+1]
                lst[i][j+1] = tmp
                
                t = func(lst, N)
                if t > maxx:
                    maxx = t
                tmp = lst[i][j]
                lst[i][j] = lst[i][j+1]
                lst[i][j+1] = tmp
            if i+1 < N and lst[i][j] != lst[i+1][j]:
                tmp = lst[i][j]
                lst[i][j] = lst[i+1][j]
                lst[i+1][j] = tmp
                
                t = func(lst, N)
                if t > maxx:
                    maxx = t
                tmp = lst[i][j]
                lst[i][j] = lst[i+1][j]
                lst[i+1][j] = tmp

print(maxx)
import sys

inpuq = sys.stdin.readline


N = int(input())

lst = []

for i in range(N):
    ar = list(map(int, input().split()))
    lst.append(ar)


minn = 100000000

def tour(route, day, visited):
    global minn

    if len(route) == N:
        cur = route[-1]
        start = route[0]
        if lst[cur][start] != 0:
            
            day += lst[cur][start]
            if minn > day:
                minn = day
            return

    cur = route[-1]
    

    for i in range(N):
        if visited[i] == 0 and lst[cur][i] != 0 and day < minn:
            
            temp = route[:]
            temp.append(i)
            
            visited[i] = 1
            tour(temp, day+lst[cur][i], visited)
            visited[i] = 0



for i in range(N):
    r = []
    r.append(i)

    v = [0]*N
    v[i] = 1

    tour(r, 0, v)

print(minn)
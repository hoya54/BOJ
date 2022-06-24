import sys

input = sys.stdin.readline

n, l, r = map(int, input().split())

ar = []

for _ in range(n):
    st = list(map(int, input().split()))
    ar.append(st)

def find(x, p):
    if p[x] == x:
        return x
    else:
        return find(p[x], p)

def union(a, b, p):
    #print("union", a, b)
    ta = find(a, p)
    tb = find(b, p)

    if ta < tb:
        p[tb] = ta
    else:
        p[ta] = tb



dx = [0, 1]
dy = [1, 0]
cnt = 0

while True:
    bench = [[] for i in range(n*n)]
    p = [i for i in range(n*n)]

    for i in range(n):
        for j in range(n):
            for k in range(2):
                nx = i+dx[k]
                ny = j+dy[k]

                if 0 <= nx < n and 0 <= ny < n and l <= abs(ar[i][j] - ar[nx][ny]) <= r:
                    left = find(i*n + j, p)
                    right = find(nx*n + ny, p)
                    #print("union", i*n+j, nx*n+ny)
                    union(left, right, p)
    
    for i in range(n*n):
        bench[find(i, p)].append(i)
    #print("bench", bench)

    flag = 0

    for u in bench:
        #print(u)
        if len(u) <= 1:
            continue
        else:
            flag = 1

            summ = 0
            for c in u:
                summ += ar[c//n][c%n]
            avg = summ//len(u)
            #print("avg", avg)
            for c in u:
                ar[c//n][c%n] = avg

    if flag == 0:
        break
    else:
        cnt += 1
    
    #for i in range(n):
    #    print(ar[i])
    #print()

print(cnt)





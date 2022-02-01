import sys

input = sys.stdin.readline

n, M = map(int, input().split())

ar = [[9999999 for col in range(n+1)] for row in range(n+1)]
result = [0]*(n+1)
for i in range(0, M):
    a, b = map(int, input().split())
    ar[a][b]=1
    ar[b][a]=1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1): 
                ar[i][j] = min(ar[i][j], ar[i][k]+ar[k][j])

minn=999999999
mi=0

for i in range(1, n+1):
    summ=0
    for j in range(1, n+1):
        if i != j:
            summ += ar[i][j]
    if minn > summ:
        minn = summ
        mi = i

print(mi)


    

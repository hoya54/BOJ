import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(N)]

r_min=10000000000000000000000
      
r_high=-1

for r in range(0, 257):
    summ=0
    a=0
    b=0
    for i in range(0, N):
        for j in range(0, M):
            if lst[i][j] > r:
                a = a + (lst[i][j]-r)
            else:
                b = b + (r-lst[i][j])
    if a+B<b:
        continue
    summ = 2*a+b
    if r_min >= summ:
        r_min = summ
        r_high = r

print(r_min, r_high)
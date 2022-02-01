import sys
input = sys.stdin.readline

N = int(input())

st = str(N)
minn=N

for i in range(1, N+1):
    st_sum =0
    st_i = str(i)
    for j in range(0, len(st_i)):
        st_sum = st_sum + int(st_i[j])

    if i+st_sum == N and minn > i:
        minn = i

if minn == N:
    minn = 0
print(minn)
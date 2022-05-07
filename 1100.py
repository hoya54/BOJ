import sys

input = sys.stdin.readline

ar = [[0]*8 for _ in range(8)]

for i in range(8):
    st = input().rstrip()
    for j in range(8):
        ar[i][j] = st[j]

w = 0
cnt = 0

for i in range(8):
    for j in range(8):
        if ar[i][j] == 'F' and (i+j)%2 == 0:
            cnt += 1

print(cnt)
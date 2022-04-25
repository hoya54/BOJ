import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

ar = [[0 for _ in range(N)] for _ in range(N)]

houses = []
bbqs = []

for i in range(N):
    st = list(map(int, input().split()))
    for j in range(N):
        ar[i][j] = st[j]
        if st[j] == 1:
            houses.append((i, j))
        elif st[j] == 2:
            bbqs.append((i, j))

min_distance = 10000
for bbq_lst in combinations(bbqs, M):
    sum_distance = 0
    for house in houses:
        minn = 10000
        for bbq in bbq_lst:
            distance = abs(house[0] - bbq[0]) + abs(house[1] - bbq[1])
            if distance < minn:
                minn = distance
        sum_distance += minn
    if sum_distance < min_distance:
        min_distance = sum_distance

print(min_distance)


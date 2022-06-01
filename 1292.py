
ar = [0]*1001

cur = 1
for i in range(1, 1001):
    for j in range(i):
        ar[cur] = i
        cur += 1
        if cur == 1001:
            break
    if cur == 1001:
            break

summ = 0

x, y = map(int, input().split())

summ = sum(ar[x:y+1])
print(summ)
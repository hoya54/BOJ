n = int(input())

prime = [0]*2000001
p = []
for i in range(2, 2000001):
    if prime[i] == 0:
        p.append(i)
        for j in range(i, 2000001, i):
            prime[j] = 1

for i in p:
    if i < n:
        continue
    else:
        t = str(i)[::-1]
        if str(i) == t:
            print(i)
            break

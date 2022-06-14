import math

n = int(input())

maxx = 2000001

prime = [0]*maxx
p = []


for i in range(2, int(math.sqrt(maxx))+1):
    if prime[i] == 0:
        p.append(i)
        for j in range(i, maxx, i):
            prime[j] = 1

for i in p:
    if i < n:
        continue
    else:
        t = str(i)[::-1]
        if str(i) == t:
            print(i)
            break

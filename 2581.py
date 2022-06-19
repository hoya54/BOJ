M = int(input())
N = int(input())

prime = [1]*10001
prime[0] = 0
prime[1] = 0



for i in range(2, 10001):
    if prime[i] == 1:
        for j in range(i+i, 10001, i):
            prime[j] = 0

lst = []

for i in range(M, N+1):
    if prime[i] == 1:
        lst.append(i)

if len(lst) == 0:
    print(-1)
else:
    print(sum(lst))
    print(lst[0])
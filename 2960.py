n, k = map(int, input().split())

prime = [0]*(n+1)
cnt = 0

for i in range(2, n+1):
    if prime[i] == 0:
        prime[i] = 1
        cnt += 1
        if cnt == k:
            print(i)
            break
        for j in range(i+i, n+1, i):
            if prime[j] == 0:
                prime[j] = 1
                cnt += 1
                if cnt == k:
                    print(j)
                    break
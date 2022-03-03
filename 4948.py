import sys

input = sys.stdin.readline

lst = [1]*246913 # 1은 소수 0은 소수아님
lst[0] = 0
lst[1] = 0
lst[2] = 1


for i in range(2, int(246913 **0.5)+1):
    if lst[i] == 1:
        for j in range(i+i, 246913, i):
            lst[j] = 0
    else:
        continue


summ = [0]* 246913

for i in range(2, 246913):
    summ[i] = summ[i-1] + lst[i]



while True:
    n = int(input())
    if n == 0:
        break

    print(summ[2*n] - summ[n])

    
n = int(input())

cnt = 0

lst = [500, 100, 50, 10, 5, 1]

n = 1000 - n

for i in lst:
    cnt += (n//i)
    n = n%i

print(cnt)

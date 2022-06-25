origin = int(input())

cnt = 0
n = origin

while True:
    
    n = n%10*10 + (n//10+n%10)%10
    cnt += 1

    if n == origin:
        break
    
print(cnt)

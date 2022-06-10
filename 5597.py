
lst = [0]*30

for i in range(28):
    n = int(input())
    lst[n-1] = 1

for i in range(30):
    if lst[i] == 0:
        print(i+1)
import sys

input = sys.stdin.readline

ar = [False]*10001

for i in range(1, 10001):
    if(ar[i] == True):
        continue

    while True:
        temp = str(i)
        for t in range(len(temp)):
            i += int(temp[t])

        if(i <= 10000):
            ar[i] = True
        else:
            break

for i in range(1, 10001):
    if(ar[i] == False):
        print(i)
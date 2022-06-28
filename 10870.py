n = int(input())

ar = [0]*21

ar[1] = 1

for i in range(2, 21):
    ar[i] = ar[i-2] + ar[i-1]

print(ar[n])
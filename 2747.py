n = int(input())

a = [0] * 46
a[1] = 1

for i in range(2, 46):
    a[i] = a[i-2] + a[i-1]

print(a[n])
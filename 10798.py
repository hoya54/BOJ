
ar = [[-1 for _ in range(15)] for _ in range(15)]

for i in range(5):
    st = input()
    for j in range(len(st)):
        ar[j][i] = st[j]

for i in range(15):
    for j in range(5):
        if ar[i][j] != -1:
            print(ar[i][j], end='')
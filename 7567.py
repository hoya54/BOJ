st = input().rstrip()

s = 10

for i in range(1, len(st)):
    if st[i-1] == st[i]:
        s += 5
    else:
         s += 10

print(s)


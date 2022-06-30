lst = []
for i in range(8):
    lst.append(int(input()))

d = lst[:]
d.sort(reverse=True)

result = []
total = 0

for i in range(5):
    total += d[i]

    result.append(lst.index(d[i])+1)

print(total)
result.sort()
print(*result)
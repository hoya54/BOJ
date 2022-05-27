s = 0

for i in range(5):
    n = int(input())

    if n < 40:
        n =40
    s += n
print(s//5)

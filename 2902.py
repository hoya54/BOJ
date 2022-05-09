st = list(input().split('-'))

r = []
for i in st:
    r.append(i[0])
    
print(''.join(map(str, r)))

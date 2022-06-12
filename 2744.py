

st = list(input().rstrip())

for i in range(len(st)):
    if st[i].isupper():
        st[i] = st[i].lower()
    else:
        st[i] = st[i].upper()

print(''.join(map(str, st)))




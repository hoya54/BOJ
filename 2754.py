st = input()

g = ''
if st[0] == 'A':
    if st[1] == '+':
        g = '4.3'
    elif st[1] == '0':
        g = '4.0'
    else:
        g = '3.7'
elif st[0] == 'B':
    if st[1] == '+':
        g = '3.3'
    elif st[1] == '0':
        g = '3.0'
    else:
        g = '2.7'
elif st[0] == 'C':
    if st[1] == '+':
        g = '2.3'
    elif st[1] == '0':
        g = '2.0'
    else:
        g = '1.7'
elif st[0] == 'D':
    if st[1] == '+':
        g = '1.3'
    elif st[1] == '0':
        g = '1.0'
    else:
        g = '0.7'
else:
    g = '0.0'

print(g)
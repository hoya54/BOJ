n = int(input())

for i in range(0, n):
    sum=0
    st = input()
    length = len(st)
    sc=0
    if st[0]=="O":
        sum += 1
    plus = 1
    for j in range(1, length):
        if st[j-1]=="O" and st[j]=="O":
            plus += 1
            sum += plus
        elif st[j-1]=="O" and st[j]=="X":
            plus = 1
        elif st[j-1]=="X" and st[j]=="O":
            plus = 1
            sum += 1
        else:
            plus = 1
    print(sum)
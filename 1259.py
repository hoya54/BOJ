while(True):
    st = input()
    if st=="0":
        break
    length = len(st)
    half = int(length/2)
    result = 1
    for i in range(0, half):
        if st[i] != st[length -1 -i]:
            result = 0
            break
    if result == 1:
        print("yes")
    else:
        print("no")
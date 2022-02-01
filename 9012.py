from collections import deque

N = int(input()) 
for i in range(0, N):
    state = "YES"
    st = input()
    d = deque()
    for j in range(0, len(st)):
        if st[j] == "(":
            d.append(st[j])
        else:
            if len(d) != 0:
                temp = d.pop()
                d.append(temp)
            else:
                state = "NO"
                break
            if temp == "(":
                d.pop()
            else:
                d.append(st[j])
    if len(d) !=0:
        state= "NO"
    print(state)

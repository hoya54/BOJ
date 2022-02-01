import sys

input = sys.stdin.readline

while True:
    d = []
    st = input().rstrip()
    
    if st == ".":
        break
    state = 1
    for c in st:
        length = len(d)
        if c == "[" or c == "(":
            d.append(c)
        elif c=="]":
            if length==0:
                state=0
                break
            if d[-1] == "[":
                d.pop()
            else:
                state=0
                break
        elif c==")":
            if length==0:
                state=0
                break
            if d[-1] == "(":
                d.pop()
            else:
                state=0
                break
    if state == 1 and length == 0:
        print("yes")
    else:
        print("no")
    
        
        

import sys

input = sys.stdin.readline

st = input().rstrip()

stack = []

tag = 0

for i in range(len(st)):
    if tag == 1:
        print(st[i], end = '')
        if st[i] == '>':
            tag = 0
        continue
    
    if st[i] == '<':
        for j in range(len(stack)):
            print(stack.pop(), end = '')
        print(st[i], end = '')
        tag = 1
    elif st[i] == ' ':
        
        for j in range(len(stack)):
            print(stack.pop(), end = '')
        print(st[i], end = '')
    else:
        stack.append(st[i])

for i in range(len(stack)):
    print(stack.pop(), end = '')
    

import sys
from collections import deque
input = sys.stdin.readline

st = input().rstrip()

stack = deque()

priority = {}
priority['('] = -1
priority[')'] = -1
priority['+'] = 1
priority['-'] = 1
priority['*'] = 2
priority['/'] = 2



for i in range(0, len(st)):
    c = st[i]
    if 'A' <= c <= 'Z':
        print(c, end='')
    elif c == '(':
        stack.append(c)
    elif c == ')':
        while stack[-1] != '(':
            t = stack.pop()
            print(t, end='')
            if len(stack)==0:
                break
        stack.pop()
    else:
        if len(stack) == 0:
            stack.append(c)
        elif priority[stack[-1]] < priority[c]:
            stack.append(c)
        else:
            while priority[stack[-1]] >= priority[c]:
                t = stack.pop()
                print(t, end='')
                if len(stack)==0:
                    break
            stack.append(c)


while len(stack) != 0:
    c = stack.pop()
    print(c, end='')
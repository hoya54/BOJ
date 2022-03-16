import sys


input = sys.stdin.readline

st = input().rstrip()


stack = []
result = 0

tmp = 1

for i in range(len(st)):
    if st[i] == '(':
        stack.append(st[i])
        tmp *= 2
    elif st[i] == ')':
        if len(stack) == 0 or stack[-1] != '(':
            result = 0
            break
        else:
            stack.pop()
            if st[i-1] == '(':
                result += tmp
            tmp //=2

    elif st[i] == '[':
        stack.append(st[i])
        tmp *= 3
    else:
        if len(stack) == 0 or stack[-1] != '[':
            result = 0
            break
        else:
            stack.pop()
            if st[i-1] == '[':
                result += tmp
            tmp //=3


if stack:
    result = 0

print(result)

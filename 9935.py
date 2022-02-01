import sys

input = sys.stdin.readline

st = input().rstrip()

t = input().rstrip()

last = t[-1]
t_len = len(t)

stack = []

for i in st:
    stack.append(i)
    if i == last and len(stack) >= t_len:
        same = True
        for i in range(-1, (-len(t))-1, -1):
            if stack[i] != t[i]:
                same =  False
                break

        if same == True :
            for j in range(t_len):
                stack.pop()
    

if len(stack) == 0:
    print("FRULA")
else:
    for i in range(0, len(stack)):
        print(stack[i], end='')
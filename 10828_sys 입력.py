import sys
input = sys.stdin.readline
N = int(input())

top = -1
stack = []

for i in range(0, N):
    st = input().split()
    if st[0] == "push":
        stack.append(st[1])
        top += 1

    elif st[0] == "pop":
        if top==-1:
            print(-1)
        else:
            print(stack.pop())
            top -= 1

    elif st[0] == "size":
        print(top+1)

    elif st[0] == "empty":
        if top == -1:
            print(1)
        else:
            print(0)
            
    elif st[0] == "top":
        if top==-1:
            print(-1)
        else:
            print(stack[top])
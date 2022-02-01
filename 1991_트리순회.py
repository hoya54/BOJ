import sys

input = sys.stdin.readline

N = int(input())

tree = {}
for i in range(N):
    parent, left, right = input().split()
    tree[parent] = (left, right)

def preorder(x):
    if x == '.':
        return
    else:
        print(x, end='')
        preorder(tree[x][0])
        preorder(tree[x][1])

def inorder(x):
    if x == '.':
        return
    else:
        inorder(tree[x][0])
        print(x, end='')
        inorder(tree[x][1])

def postorder(x):
    if x == '.':
        return
    else:
        postorder(tree[x][0])
        postorder(tree[x][1])
        print(x, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
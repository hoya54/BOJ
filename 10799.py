import sys

input = sys.stdin.readline

ar = input().rstrip()

count = 0
layer = 0

for i in range(len(ar)):
    #print(ar[i], end = ' ')
    if ar[i] == '(':
        if ar[i+1] == ')':
            count += layer
        else:
            layer += 1
    else:
        if ar[i-1] == '(':
            #print(count, layer)
            continue
        else:
            count += 1
            layer -= 1
    #print(count, layer)

print(count)
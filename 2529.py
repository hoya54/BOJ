import sys

input = sys.stdin.readline

N = int(input())
ar = list(map(str, input().split()))

result_min = []
result_max = []
flag = 0

def func(x, depth, lst):
    #print(lst)
    global result_min
    global result_max
    global start, end, iter
    global flag

    if depth == N:
        if not result_min:
            result_min = lst[:]
            start, end, iter = 9, -1, -1
        else:
            result_max = lst[:]
        return

    for i in range(start, end, iter):
        if i in lst:
            continue

        if ar[depth] == '>':
            if x > i:
                lst.append(i)
                func(i, depth+1, lst)
                lst.pop()
        else:
            if x < i:
                lst.append(i)
                func(i, depth+1, lst)
                lst.pop()

        if result_min and flag == 0:
            break
        if result_max:
            break

start, end, iter = 0, 10, 1

for i in range(start, end, iter):
    func(i, 0, [i])
    if result_min:
        break

flag = 1

for i in range(start, end, iter):
    func(i, 0, [i])
    if result_max:
        break


print(''.join(map(str, result_max)))
print(''.join(map(str, result_min)))

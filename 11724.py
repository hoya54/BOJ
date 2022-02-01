import sys
input = sys.stdin.readline

N, M = map(int, input().split())


lst = [0]*(N+1)

for i in range(1, N+1):
    lst[i] = i

def find_parent(a):
    global lst

    if lst[a] == a:
        return a
    else:
        p = find_parent(lst[a])
        lst[a] = p
        return p

for i in range(0, M):
    a, b = map(int, input().split())
    if b < a:
        tmp = a
        a = b
        b = tmp
    parent_a = find_parent(a)
    parent_b = find_parent(b)
    if parent_b < parent_a:
        tmp = parent_a
        parent_a = parent_b
        parent_b = tmp
    #print(parent_a, parent_b)
    if parent_a != parent_b:
        lst[parent_b] = parent_a
    #print(lst)


result=[0]*(N+1)
for i in range(1, N+1):
    result[i] = find_parent(i)
print(len(set(result))-1)
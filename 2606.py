import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

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
    if parent_a != parent_b:
        lst[parent_b] = parent_a
summ=0
for i in range(2, N+1):
    if find_parent(i)==find_parent(1):
        summ += 1
print(summ)
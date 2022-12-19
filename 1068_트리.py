import sys

input = sys.stdin.readline

n = int(input())

parents = list(map(int, input().split()))

target = int(input())

childs = [[] for _ in range(n)]
deleted = [0]*n
root = -1

for node in range(n):
    p = parents[node]
    if(p == -1):
        root = node
        continue
    childs[p].append(node)


def delete_child(t):
    global parents
    global childs
    global deleted

    parent_of_t = parents[t]
    childs[parent_of_t].remove(t)
    deleted[t] = 1

    bench = childs[t][:]

    for child_of_t in bench:
        delete_child(child_of_t)


if target == root:
    print(0)
else:
    delete_child(target)

    cnt = 0
    for i in range(n):
        if(len(childs[i]) == 0 and deleted[i] == 0):
            cnt += 1

    print(cnt)
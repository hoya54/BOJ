import sys

input = sys.stdin.readline

N = int(input())

x, y = map(int, input().split())

m = int(input())

c_p = [i for i in range(N+1)]

for i in range(m):
    p, c = map(int, input().split())

    c_p[c] = p

    
def find(a, c_p, lst):
    
    if c_p[a] == a:
        return lst
    else:
        lst.append(c_p[a])
        find(c_p[a], c_p, lst)
        return lst


x_lst = find(x, c_p, [x])
y_lst = find(y, c_p, [y])


if x_lst[-1] == y_lst[-1]:
    
    x_set = set(x_lst)
    y_set = set(y_lst)
    inter = x_set.intersection(y_lst)

    print(len(x_set - inter) + len(y_set - inter))
else:
    print(-1)
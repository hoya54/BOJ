import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
result = [0]*n

t = []
for i in range(n):
    while t:
        if lst[t[-1]] < lst[i]:
            t.pop()
        else:
            result[i] = t[-1] +1
            break

    t.append(i)

print(*result)
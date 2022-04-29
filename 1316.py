import sys

input = sys.stdin.readline

n = int(input())

cnt = 0
for _ in range(n):
    st = input().rstrip()

    if len(st) == 1:
        cnt += 1
    else:
        r = 1
        s = set()
        s.add(st[0])
        for i in range(1, len(st)):
            if st[i] == st[i-1]:
                continue
            if st[i] not in s:
                s.add(st[i])
                continue
            else:
                r = 0
                break
        cnt += r

print(cnt)
            
import sys
input = sys.stdin.readline

M = int(input())

s = set()

for i in range(0, M):
    st = list(input().split())
    if len(st)==2:
        value = int(st[1])

    if st[0]=="add":
        s.add(value)
    elif st[0]=="remove":
        if value in s:
            s.remove(value)
    elif st[0]=="check":
        if value in s:
            print(1)
        else:
            print(0)
    elif st[0]=="toggle":
        if value in s:
            s.remove(value)
        else:
            s.add(value)
    elif st[0]=="all":
        s.clear()
        s.update([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    else:
        s.clear()
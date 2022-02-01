import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

def pr(lst, r):
    if len(lst)==0:
        print('[]')
        return
    if r==-1:
        lst = list(lst)
    else:
        lst = list(lst)
        lst.reverse()

    print('[',end="")
    for i in range(0, len(lst)-1):
        print(lst[i], end=',')
    print("{0}".format(lst[len(lst)-1]), end=']\n')


for i in range(0, T):
    st = input().rstrip()
    length = int(input())

    ar = input()
    ar = ar.replace('[', '')
    ar = ar.replace(']', '')
    ar = ar.replace(',', ' ')
    ar = list(map(int, ar.split()))

    lst = deque()

    r=-1
    
    for j in range(0, length):
        lst.append(ar[j])
    
    er=0
    for j in range(0, len(st)):
        c = st[j]

        if c == 'R':
            r = r*(-1)
        else:
            if len(lst)==0:
                print("error")
                er=1
                break
            else:
                if r == -1:
                    lst.popleft()
                else:
                    lst.pop()
    if er == 0:
        pr(lst, r)
    
        

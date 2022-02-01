import sys

input = sys.stdin.readline

T = int(input())

for i in range(0, T):
    N, M = input().split()
    N=int(N)
    M=int(M)

    lst = list(map(int, input().split()))
    count=1
    index=0
    target = M
    while True:
        if target == 0:
            if max(lst) == lst[0]:
                print(count)
                break
            else:
                temp = lst[0]
                lst.append(temp)
                del lst[0]
                target = len(lst)-1
                #count += 1

        else:
            if max(lst) == lst[0]:
                del lst[0]
                count += 1
            else:
                temp = lst[0]
                lst.append(temp)
                del lst[0]
            target -=1
            



import sys
input = sys.stdin.readline

N, M = map(int, input().split())

lst=[]
for i in range(0, N):
    a = input()
    lst.append([a, i])

chr_lst = sorted(lst)

def find_chr(lst, start, end, target, index):
    if start > end:
        return -1
    mid = (start+end)//2
    
    if lst[mid][index] == target:
        return mid

    elif lst[mid][index] > target:
        return find_chr(lst, start, mid-1, target, index)

    else:
        return find_chr(lst, mid+1, end, target, index)

result=[]
for i in range(1, M+1):
    a = input()
    if "A" <= a[0] <="Z":
        result.append(chr_lst[find_chr(chr_lst, 0, N, a, 0)][1]+1)
    else:
        result.append(lst[find_chr(lst, 0, N, int(a)-1, 1)][0])
for i in range(0, M):
    a = str(result[i])

    a = a.replace('\n', '')
    print(a)
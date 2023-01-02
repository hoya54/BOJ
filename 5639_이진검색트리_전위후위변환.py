import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**9)

lst = []

while True:
    try:
        lst.append(int(input()))
    except:
        break

n = len(lst)

def func(start, end):
    # print("func x = ", start)
    if(start > end):
        return

    mid = end+1

    for i in range(start+1, end+1):
        if(lst[start] < lst[i]):
            mid = i
            break


    func(start+1, mid-1)
    func(mid, end)

    print(lst[start])

    

func(0, n-1)
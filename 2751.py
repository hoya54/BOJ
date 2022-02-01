N = int(input())
lst=[]

for i in range(0, N):
    a = int(input())
    lst.append(a)
lst.sort()

for i in range(0, N):
    print(lst[i])
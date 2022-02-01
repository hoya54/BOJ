N = int(input())
lst =[]

for i in range(0, N):
    temp = input()
    lst.append(temp)

lst = set(lst)
lst = list(lst)
lst.sort(key=lambda x : (len(x), x))

for i in range(0, len(lst)):
    print(lst[i])
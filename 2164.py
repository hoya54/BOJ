N = int(input())
lst=[]
for i in range(1, N+1):
    lst.append(i)

del_index = 0
move_index = 1
index = N-1

ind = N-1
i=0
while(True):
    if i%2==1:
        temp = lst[i]
        lst.append(temp)
        ind = ind+1
    if lst[ind-1] == lst[ind]:
        break
    i = i+1

print(lst[ind])
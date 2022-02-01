N, K = input().split()
N = int(N)
K = int(K)

index=0
total=N
lst=[]

for i in range(1, N+1):
    lst.append(i)

result=[]
for i in range(0, N):
    index = (index + K-1)%total
    result.append(lst[index])
    del lst[index]
    total -= 1

print("<", end="")
for i in range(0, N-1):
    print("{0}, ".format(result[i]), end="")
print("{0}>".format(result[N-1]))
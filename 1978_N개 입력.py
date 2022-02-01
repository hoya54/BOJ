N = int(input())

nums = list(map(int, input().split()))

def func(a):
    if a==1:
        return False
    for i in range(2, a):
        if a%i==0:
            return False
    return True

sum=0

for i in range(0, N):
    result = func(nums[i])
    if result == True:
        sum += 1
print(sum)
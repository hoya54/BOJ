import sys

input = sys.stdin.readline


n = int(input())

ar = [[0 for _ in range(3)] for _ in range(n)]

for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(3):
        ar[i][j] = lst[j]

dp_max = [ar[0][0], ar[0][1], ar[0][2]]
dp_min = [ar[0][0], ar[0][1], ar[0][2]]
temp_max = [0,0,0]
temp_min = [0,0,0]

for i in range(1, n):
    for j in range(3):
        if(j == 0):
            temp_max[j] = ar[i][j] + max(dp_max[j], dp_max[j+1])
            temp_min[j] = ar[i][j] + min(dp_min[j], dp_min[j+1])
        elif(j == 1):
            temp_max[j] = ar[i][j] + max(dp_max[j-1], dp_max[j], dp_max[j+1])
            temp_min[j] = ar[i][j] + min(dp_min[j-1], dp_min[j], dp_min[j+1])
        else:
            temp_max[j] = ar[i][j] + max(dp_max[j-1], dp_max[j])
            temp_min[j] = ar[i][j] + min(dp_min[j-1], dp_min[j])
    dp_max = temp_max[:]
    dp_min = temp_min[:]

print(max(dp_max), min(dp_min))
        

        


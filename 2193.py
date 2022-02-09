import sys

input = sys.stdin.readline
 
N = int(input())

arr0 = [0]*91
arr1 = [0]*91

arr1[1] = 1

for i in range(2, N+1):
    arr0[i] = arr0[i-1] + arr1[i-1]
    arr1[i] = arr0[i-1]

print(arr0[N] + arr1[N])
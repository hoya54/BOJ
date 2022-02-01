import sys

input = sys.stdin.readline

N = int(input())

i=665
count=0
state=1
while count != N:
    i += 1
    if "666" in str(i):
        count += 1
    
print(i)
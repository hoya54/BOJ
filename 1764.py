import sys
input = sys.stdin.readline

N, M = map(int, input().split())

s1 = set()
s2 = set()
for i in range(0, N):
    s1.add(input())

for i in range(0, M):
    s2.add(input())

#s3 = s1.intersection(s2)
s3 = s1&s2

print(len(s3))
s3 = list(s3)
s3.sort()
for i in range(0, len(s3)):
    print(s3[i].rstrip())
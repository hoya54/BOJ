import sys

input = sys.stdin.readline

N = int(input())
lst=[]

for i in range(0, N):
    a, b = map(int, input().split())
    lst.append([a, b])

# 1번 인덱스 정렬 후 0번 인덱스 정렬
lst.sort(key=lambda x:(x[1],x[0]))

cnt=1
end = lst[0][1]
for i in range(1, N):
    if end <= lst[i][0]:
        cnt += 1
        end = lst[i][1]
print(cnt)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dic = {}
for i in  range(0, N):
    addr, k = input().split()
    addr = addr.rstrip()
    dic[addr] = k

result = []
for i in range(0, M):
    st = input().rstrip()
    result.append(dic[st])

for i in result:
    print(i)
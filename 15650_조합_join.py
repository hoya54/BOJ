import sys
import itertools 

input = sys.stdin.readline

N, M = map(int, input().split())
lst = []
for i in range(1, N+1):
    lst.append(i)

for i in itertools.combinations(lst, M):
    print(' '.join(map(str, i))) 
    # 리스트 값들을 map으로 문자열로 만들고 
    # 각 요소들을 join으로 문자열로 만들어서 '' 사이의 값을 각 요소 사이에 넣음
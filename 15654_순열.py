import sys
import itertools 

input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

for i in itertools.permutations(lst, M):
    print(' '.join(map(str, i))) 
    # 리스트 값들을 map으로 문자열로 만들고 
    # 각 요소들을 join으로 문자열로 만들어서 '' 사이의 값을 각 요소 사이에 넣음
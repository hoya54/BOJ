import sys


input = sys.stdin.readline

N, M = map(int, input().split())

def counter(n, k):
    cnt = 0
    while n:
        n //= k
        cnt += n
    return cnt

five_cnt = counter(N, 5) - counter(M, 5) - counter(N-M, 5)
two_cnt = counter(N, 2) - counter(M, 2) - counter(N-M, 2)

print(min(five_cnt, two_cnt))
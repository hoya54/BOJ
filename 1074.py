import sys

input = sys.stdin.readline

N, r, c = map(int, input().split())

count = 0
# sx, sy : 검색 시작지점의 x, y 좌표
# tx, ty : 입력값 r, c 
def func(n, sx, sy, tx, ty):
    global ar
    global flag
    global count

    if n >1:
        if tx <sx+2**(n-1)  and ty < sy+2**(n-1): # 2사분면
            func(n-1, sx, sy, tx, ty)
        elif tx <sx+2**(n-1) and sy+2**(n-1) <= ty: # 3사분면
            count += 4**(n-1)
            func(n-1, sx, sy+2**(n-1), tx, ty)
        elif sx+2**(n-1) <= tx and ty < sy+2**(n-1): # 1사분면
            count += 2*4**(n-1)
            func(n-1, sx+2**(n-1), sy, tx, ty)
        else:                                        # 4사분면
            count += 3*4**(n-1)
            func(n-1, sx+2**(n-1), sy+2**(n-1), tx, ty)
        
    else:
        if sx == tx and sy == ty:
            print(count)
        elif sx == tx and sy+1 == ty:
            print(count+1)
        elif sx+1 == tx and sy == ty:
            print(count+2)
        elif sx+1 == tx and sy+1 == ty:
            print(count+3)
        
func(N, 0, 0, r, c)

import sys
input = sys.stdin.readline

N = int(input())

if N==4 or N==7:
    print(-1)
elif N==3 or N==5:
    print(1)
elif N==6 or N==8:
    print(2)
elif N==9:
    print(3)
else:
    r =  N%5
    if r == 0:
        print(int(N/5))
    elif r==1 or r==3:
        print(int(N/5)+1)
    else:
        print(int(N/5)+2)

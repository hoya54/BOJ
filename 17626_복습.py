import sys
import math

input = sys.stdin.readline

N = int(input())

e = math.sqrt(N)
e = int(e)

summ = []

for i in range(1, e+1):
    summ.append(i**2)

state=0
if N in summ:
    state=1
    print(1)


def func2():
    global summ
    global N
    global e
    global state

    for i in range(0, e):
        for j in range(i, e):
            if summ[i]+summ[j]==N:
                state=1
                print(2)
                return

def func3():
    global summ
    global N
    global e
    global state

    for i in range(0, e):
        for j in range(i, e):
            for k in range(j, e):
                if summ[i]+summ[j]+summ[k]==N:
                    state=1
                    print(3)
                    return                
if state==0:
    func2()
if state == 0:
    func3()
if state == 0:
    print(4)
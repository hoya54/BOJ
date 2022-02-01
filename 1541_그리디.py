import sys
import itertools

input = sys.stdin.readline

st = input().rstrip()

num = []

op = []

for i in range(0, len(st)):
    if st[i] == '+' or st[i] == '-':
        op.append(st[i])

st = st.replace('+', ' ')
st = st.replace('-', ' ')

num = list(map(int, st.split()))

lst =[]
for i in range(0, len(op)):
    lst.append(i)

def cal(num, op):

    i=0
    while True:
        if i >= len(op):
            break

        o = op[i]
        if o == '+':
            left = i
            right = i+1
            r = num[left]+num[right]
            del op[i]
            i -= 1
            del num[right]
            num[left] = r

            minn=r
            #print(num)
        i += 1

        
            
    minn = num[0]
    for i in range(1, len(num)):
        minn = minn - num[i]
    
    return minn


x = cal(num, op)
    #print(result[i])
    
print(x)


import sys
input = sys.stdin.readline

N = int(input())
lst=[]
summ=0
minn = 5000
maxx = -5000
count = [0] * 8001
for i in range(0, N):
    a = int(input())
    if a > maxx:
        maxx = a
    if a < minn:
        minn = a
    lst.append(a)
    summ=summ+a
    count[a+4000] += 1

lst.sort()
print("%.0f" % (summ/N))
print("%d" % lst[int(N/2)])

M = max(count)
st=[]
for i in range(0, 8001):
    if count[i]==M:
        st.append(i)
    if len(st) >= 2:
        break

if len(st) >= 2:
    print(st[1]-4000)
else:
    print(st[0]-4000)
print(maxx-minn)

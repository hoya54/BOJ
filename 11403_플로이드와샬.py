import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())

ar = []
visited=[0]*N

for i in range(0, N):
    st = list(map(int, input().split()))
    ar.append(st)

def func(ar, visit, ox, x, y):
    
    global N
    
    state=0
    if visit[x]==1:
        return 0

    visit[x]=1

    for i in range(0, N):
        if ar[x][i] == 1:
            if i == y:
                state =  1
                break
            else:
                state = func(ar, visit, ox, i, y)
                if state==1:
                    break

    return state


for i in range(0, N):
    for j in range(0, N):
        for k in range(0, N):
            visited[k]=0
        r=0
        if i==j and ar[i][j] == 1:
            r=1
        else:
            r = func(ar, visited, i, i, j)
        print(r, end=" ")
    print()
        

# 플로이드 와샬 
# for k in range(N):
#     for i in range(N):
#         for j in range(N): 
#             if ar[i][j] == 1 or (ar[i][k] == 1 and ar[k][j] == 1):
#                 ar[i][j] = 1
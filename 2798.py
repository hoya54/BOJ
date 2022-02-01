N, goal = input().split()
N = int(N)
goal = int(goal)

lst = input().split()

closest = 0

for a in range(0, N-2):
    for b in range(a+1, N-1):
        for c in range(b+1, N):
            if a==b or a==c or b==c:
                continue
            temp = int(lst[a])+int(lst[b])+int(lst[c])
            if goal - temp >= 0 and closest < temp:
                closest = temp
print(closest)
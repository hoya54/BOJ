from collections import deque

n = int(input())

d = deque()
visited = [0]*(n+1)

d.append((n, [n]))

while d:
    n, lst = d.popleft()

    if n == 1:
        break
    
    if visited[n] == 0:
        visited[n] = 1
        
        if n%3 == 0:
            d.append((n//3, lst+[n//3]))
        if n%2 == 0:
            d.append((n//2, lst+[n//2]))
        
        d.append((n-1, lst+[n-1]))
    



print(len(lst)-1)
print(*lst)

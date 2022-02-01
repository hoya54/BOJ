N = int(input())
ex = set(map(int, input().split()))


M = int(input())
search = list(map(int, input().split()))

for i in search:
    if i in ex:
        print(1)
    else:
        print(0)
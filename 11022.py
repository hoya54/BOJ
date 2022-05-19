t = int(input())

for k in range(t):
    a, b = map(int, input().split())

    print("Case #{}: {} + {} =".format(k+1, a, b), a+b)
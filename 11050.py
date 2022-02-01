def fact(n):
    if n<= 1:
        return 1
    else:
        return n * fact(n-1)


a, b = input().split()
a=int(a)
b=int(b)

print(int(fact(a)/(fact(b)*fact(a-b))))
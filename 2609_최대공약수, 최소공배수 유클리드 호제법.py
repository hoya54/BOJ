a, b = input().split()
a = int(a)
b = int(b)

if a<b:
    temp = a
    a = b
    b = temp

def gcd(a, b):
    while b !=0:
        r = a%b
        a=b
        b=r
    return a

def lcm(a, b):
    return int(a*b/gcd(a, b))

print(gcd(a, b))
print(lcm(a, b))
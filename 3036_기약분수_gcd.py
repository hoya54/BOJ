import sys
import fractions

input = sys.stdin.readline


N = int(input())

lst = list(map(int, input().split()))

for i in range(1, N):
    A = lst[0]
    B = lst[i]
    a = fractions.Fraction(B, A).numerator   # 분자
    b = fractions.Fraction(B, A).denominator # 분모
    print(str(b) + '/' + str(a))


# fractions.gcd(3, 6) : 3과 6의 최대공약수 3
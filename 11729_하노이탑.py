
N = int(input())


def func(n, before, mid, after):
    if n==1:
        print(before, after)
    else:
        func(n-1, before, after, mid)
        print(before, after)
        func(n-1, mid, before, after)

print(2**N-1)
func(N, 1, 2, 3)

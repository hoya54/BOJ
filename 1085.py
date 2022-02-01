x, y, w, h = input().split()
x = int(x)
y = int(y)
w = int(w)
h = int(h)

a = x
b = y
c = w-x
d = h-y

lst = []
lst.append(a)
lst.append(b)
lst.append(c)
lst.append(d)
print(min(lst))
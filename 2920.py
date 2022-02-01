olst = []
alst = []
blst = []
a1, a2, a3, a4, a5, a6, a7, a8 = input().split()

olst.append(a1)
olst.append(a2)
olst.append(a3)
olst.append(a4)
olst.append(a5)
olst.append(a6)
olst.append(a7)
olst.append(a8)

alst = sorted(olst)
blst = sorted(olst, reverse = True)

if olst == alst:
    print("ascending")
elif olst == blst:
    print("descending")
else:
    print("mixed")
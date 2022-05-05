import sys

input = sys.stdin.readline

st = input().rstrip()

abc = [0]*26

for c in st:
    abc[ord(c)-97] += 1

print(' '.join(map(str, abc)))
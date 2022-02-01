import sys

input = sys.stdin.readline

st = input()

lst="abcdefghijklmnopqrstuvwxyz"
for i in range(0, 26):
    print(st.find(lst[i]), end=" ")
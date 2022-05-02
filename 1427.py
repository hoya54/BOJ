import sys

input = sys.stdin.readline

st = input().rstrip()

st = list(st)
st.sort(reverse=True)

st = ''.join(st)
print(st)
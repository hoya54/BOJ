import sys

input = sys.stdin.readline

st = input().rstrip()

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for c in croatia:
  st = st.replace(c, ' ')

print(len(st))

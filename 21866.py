import sys

scores = list(map(int, input().split()))

hacker = False
beginner = False

max_socre = [100, 100, 200, 200, 300, 300, 400, 400, 500]

summ = 0

for i in range(9):
    summ += scores[i]
    if scores[i] > max_socre[i]:
        hacker = True

if hacker == True:
    print("hacker")
elif summ >= 100:
    print("draw")
else:
    print("none")
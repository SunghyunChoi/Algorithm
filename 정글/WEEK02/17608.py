import sys
r = sys.stdin.readline

n = int(r())
h = []
answer = 1

for i in range(n):
    h.append(int(r()))

compare = h.pop()

while h:
    x = h.pop()
    if x > compare:
        answer += 1
        compare = x
print(answer)

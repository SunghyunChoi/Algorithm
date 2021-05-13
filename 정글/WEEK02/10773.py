import sys
r = sys.stdin.readline

n = int(r())
stk = []
for i in range(n):
    x = int(r())
    if x:
        stk.append(x)
    else:
        stk.pop()
print(sum(stk))
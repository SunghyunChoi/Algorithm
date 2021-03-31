import sys
r = sys.stdin.readline

string = r().strip()
pattern = list(r().strip())
ptn_len = len(pattern)
stk = [];
for char in string:
    stk.append(char)
    if char == pattern[-1]:
        if stk[-1*ptn_len:] == pattern:
            del stk[-1*ptn_len:]

if stk:
    print(''.join(stk))
else:
    print("FRULA")
import sys
from collections import deque
r = sys.stdin.readline

leftStk = list(r().strip())
cmd_num = int(r())
rightStk = deque([])

for _ in range(cmd_num):
    cmd = r().strip().split(' ')
    if cmd[0]=="L":
        if leftStk:
            rightStk.appendleft(leftStk.pop()) 
    elif cmd[0]=="D":
        if rightStk:
            leftStk.append(rightStk.popleft())
    elif cmd[0]=="B":
        if leftStk:
            leftStk.pop()
    else:
        leftStk.append(cmd[1])

print(''.join(leftStk), end='')
print(''.join(rightStk))

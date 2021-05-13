import sys
r = sys.stdin.readline

n = int(r())
s = 0
for i in range(n):
    command = r().split()
    cmd = command[0]
    if cmd == 'add':
        s |= 1 << int(command[1])
    elif cmd == 'remove':
        s &= ~(1 << int(command[1]))
    elif cmd == 'check':
        if s & (1 << int(command[1])):
            print(1)
        else:
            print(0)
    elif cmd == 'toggle': 
        s ^= (1 << int(command[1]))
    elif cmd == 'all':
        s = (1 << 21) - 1
    else:
        s = 0
    

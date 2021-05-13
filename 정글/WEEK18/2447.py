import sys
r = sys.stdin.readline

N = int(r())

output = [[' ' for _ in range(N)] for _ in range(N)]

def Stars(n, y,x):
    if(n==3):
        output[y][x] = '*'
        output[y][x+1] = '*'
        output[y][x+2] = '*'
        output[y+1][x] = '*'
        output[y+1][x+2] = '*'
        output[y+2][x] = '*'
        output[y+2][x+1] = '*'
        output[y+2][x+2] = '*'
        return


    for i in range(3):
        for j in range(3):
            if(i*j == 1):
                continue
            Stars(n//3, y+i*n//3, x+n*j//3)
    return

Stars(N,0,0)
for x in output:
    print(''.join(x))
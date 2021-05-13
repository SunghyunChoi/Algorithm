import sys
r = sys.stdin.readline

y,x = map(int, r().strip().split())

soldiers = [list(r().strip()) for _ in range(x)]

home = 0
away = 0
# print(soldiers)
for row in range(x):
    for col in range(y):
        if(soldiers[row][col]):
            stk = []
            stk.append([row,col])
            color = soldiers[row][col]
            count = 0
            while(stk):
                r,c = stk.pop()
                if not soldiers[r][c]:
                    continue
                soldiers[r][c] = 0
                count += 1
                if(r > 0 and soldiers[r-1][c] == color):
                    stk.append([r-1,c])
                if(r < x-1 and soldiers[r+1][c] == color):
                    stk.append([r+1,c])
                if(c > 0 and soldiers[r][c-1] == color):
                    stk.append([r,c-1])
                if(c < y-1 and soldiers[r][c+1] == color):
                    stk.append([r,c+1])
            if color == 'W':
                home += count**2
            else:
                away += count**2
print(home, away)
            
#Best Grass
#풀덩이 집합을 다 찾아라.
import sys
r = sys.stdin.readline

def dfs(MAP, X, Y):
    stk = [(X,Y)]
    MAP[X][Y] = '.'

    while stk:
        x,y = stk.pop()
        if x<len(MAP)-1 and MAP[x+1][y]=='#':
            stk.append((x+1,y))
            MAP[x+1][y] = '.'
        if x>0 and MAP[x-1][y]=='#':
            stk.append((x-1,y))
            MAP[x-1][y] = '.'    
        if y<len(MAP[0])-1 and MAP[x][y+1]=='#':
            stk.append((x,y+1))
            MAP[x][y+1] = '.'
        if y>0 and MAP[x][y-1]=='#':
            stk.append((x,y-1))
            MAP[x][y-1] = '.'

if __name__=='__main__':
    row, column = map(int, r().strip().split())
    MAP = [list(r().strip()) for _ in range(row)]
    answer = 0

    for i in range(row):
        for j in range(column):
            if MAP[i][j]=='#':
                dfs(MAP, i, j)
                answer += 1
                
    print(answer)
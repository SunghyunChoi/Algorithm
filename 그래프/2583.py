#영역 구하기
import sys
r = sys.stdin.readline

def getArea(X, Y, maps, visited):
    visited[X][Y] = 1
    stk = [(X,Y)]
    area = 1
    height = len(maps)
    width = len(maps[0])
    while stk:
        x, y = stk.pop()
        if x>0 and maps[x-1][y]==0 and visited[x-1][y]==0:
            stk.append((x-1,y))
            visited[x-1][y] = 1
            area += 1
        if x<height-1 and maps[x+1][y]==0 and visited[x+1][y]==0:
            stk.append((x+1,y))
            visited[x+1][y] = 1
            area += 1
        if y>0 and maps[x][y-1]==0 and visited[x][y-1]==0:
            stk.append((x,y-1))
            visited[x][y-1] = 1
            area += 1
        if y<width-1 and maps[x][y+1]==0 and visited[x][y+1]==0:
            stk.append((x,y+1))
            visited[x][y+1] = 1
            area += 1
    return area
        

def solution(M,N,K):
    maps = [[0 for _ in range(N)] for _ in range(M)]
    visited = [[0 for _ in range(N)] for _ in range(M)]
    count = 0
    area = []
    for _ in range(K):
        left, bottom, right, top = map(int, r().strip().split())
        for i in range(bottom, top):
            for j in range(left, right):
                maps[i][j] = 1

    for m in maps:
        print(m)
    for i in range(M):
        for j in range(N):
            if maps[i][j]==0 and visited[i][j]==0:
                area.append(getArea(i,j,maps,visited))
                count += 1

    print(count)
    area = sorted(area)
    print(*area, end=' ')

if __name__=='__main__':
    M,N,K = map(int, r().strip().split())
    solution(M,N,K)
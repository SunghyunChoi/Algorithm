#토마토
#BFS
#1 = 익은 토마토, 0 = 익지않은, -1 = 비어있는
#모든 토마토가 익는데 걸리는 시간을 구하라.

import sys
from collections import deque
r = sys.stdin.readline


def solve():
    m,n = map(int, r().strip().split())
    tomatos = [r().strip().split() for _ in range(n)]
    stk = deque([])
    tomatoNum = 0
    tomatoRiped = 0
    answer = -1

    for i in range(n):
        for j in range(m):
            tomato = tomatos[i][j]
            if tomato == '1':
                stk.append((i,j))
                tomatoNum += 1
                tomatoRiped += 1
            elif tomato == '0':
                tomatoNum += 1
                
    while stk:
        stkLen = len(stk)
        for _ in range(stkLen):
            x, y = stk.popleft()
            
            if x>0 and tomatos[x-1][y]=='0':
                stk.append((x-1,y))
                tomatos[x-1][y]=1
                tomatoRiped += 1

            if y>0 and tomatos[x][y-1]=='0':
                stk.append((x,y-1))
                tomatos[x][y-1]=1
                tomatoRiped += 1

            if x<n-1 and tomatos[x+1][y]=='0':
                stk.append((x+1,y))
                tomatos[x+1][y]=1
                tomatoRiped += 1

            if y<m-1 and tomatos[x][y+1]=='0':
                stk.append((x,y+1))
                tomatos[x][y+1]=1
                tomatoRiped += 1   
        answer += 1
    if tomatoNum == tomatoRiped:
        print(answer)
    else:
        print(-1)

if __name__=='__main__':
    solve()
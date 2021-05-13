## 치즈
## 행 : x, 열 : y
## 1) 치즈가 모두 녹는데 걸리는 시간
## 2) 치즈가 모두 녹기 전 남아있는 칸의 개수 = melt 하면 되겠다

####################  입력  ####################
import heapq
import sys
from collections import deque, defaultdict
r = sys.stdin.readline

n,m = map(int, r().split())
chz = [list(map(int, r().split())) for _ in range(n)]
total = 0
melt = 0
visited = [[False for _ in range(m)] for _ in range(n)]
start = [0,0]
time = 0
q = deque([start])

for i in chz:
    total += i.count(1)
#################################################
while total:
    q = deque([start])
    melt = 0
    while q:
        x,y = q.popleft()
        if x>0 and visited[x-1][y] == False:
            if chz[x-1][y]:
                visited[x-1][y] = True
                chz[x-1][y] = 0
                melt += 1
            else:
                visited[x-1][y] = True
                q.append([x-1,y])
        if x<n-1 and visited[x+1][y] == False:
            if chz[x+1][y]:
                visited[x+1][y] = True
                chz[x+1][y] = 0
                melt += 1
            else:
                visited[x+1][y] = 1
                q.append([x+1,y])
        if y>0 and visited[x][y-1] == False:
            if chz[x][y-1]:
                visited[x][y-1] = True
                chz[x][y-1] = 0
                melt += 1
            else:
                visited[x][y-1] = 1
                q.append([x, y-1])
        if y<m-1 and visited[x][y+1] == False:
            if chz[x][y+1]:
                visited[x][y+1] = True
                chz[x][y+1] = 0
                melt += 1
            else:
                visited[x][y+1] = 1
                q.append([x, y+1])
    visited = [[False for _ in range(m)] for _ in range(n)]
    time += 1
    total -= melt
    print(f"time : {time}")
    for i in chz:
        print(i)
    print()

print(time)
print(melt)
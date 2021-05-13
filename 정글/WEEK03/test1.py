## 단지 번호 붙이기
## n*n 정사각형
## house_count() : 단지 내 집 개수 Count
## bfs : 전체 Map 탐색
## bfs 하면서 count 해서 전체 맵 다 방문했는지 확인해야 한다.

####################  입력  ####################
import heapq
import sys
from collections import deque, defaultdict
r = sys.stdin.readline
n = int(r())
MAP = [list(map(int, list(r().strip()))) for _ in range(n)]
total = 1
visited = [[False for _ in range(n)] for _ in range(n)]
answer = []
#################################################

def house_count(start):
    h_q = deque()
    h_q.append(start)
    visited[start[0]][start[1]] = True
    last = []
    cnt = 1
    next_poss = []
    while(h_q):
        x, y = h_q.popleft()
        if x>0 and visited[x-1][y] == False:
            if MAP[x-1][y]:
                visited[x-1][y] = True
                h_q.append([x-1,y])
                cnt += 1
            else:
                next_poss.append([x-1,y])
        if x<n-1 and visited[x+1][y] == False:
            if MAP[x+1][y]:
                visited[x+1][y] = True
                h_q.append([x+1,y])
                cnt += 1
            else:
                next_poss.append([x+1,y])
        if y>0 and visited[x][y-1] == False:
            if MAP[x][y-1]:
                visited[x][y-1] = True
                h_q.append([x,y-1])
                cnt += 1
            else:
                next_poss.append([x,y-1])
        if y<n-1 and visited[x][y+1] == False:
            if MAP[x][y+1]:
                visited[x][y+1] = True
                h_q.append([x,y+1])
                cnt += 1
            else:
                next_poss.append([x,y+1])
    return cnt, next_poss

q = []
cnt = 0
if MAP[0][0] == 0:
    start = [0,0]
    q = deque([start])
    visited[0][0] = True
else:
    cnt, next_poss = house_count([0,0])
    total += cnt
    answer.append(cnt)
    q = deque(next_poss)
while q:
    x,y = q.popleft()
    cnt = 0
    if x>0 and visited[x-1][y] == False:
        if MAP[x-1][y]:
            cnt, next_poss = house_count([x-1,y])
            answer.append(cnt)
            total += cnt
            q.extend(next_poss)
        else:
            total += 1
            visited[x-1][y] = True
            q.append([x-1,y])
    if x<n-1 and visited[x+1][y] == False:# and MAP[x+1][y]:
        if MAP[x+1][y]:
            cnt,next_poss = house_count([x+1,y])
            answer.append(cnt)
            total += cnt
            q.extend(next_poss)
        else:
            total += 1
            visited[x+1][y] = True
            q.append([x+1,y])
    if y>0 and visited[x][y-1] == False:# and MAP[x][y-1]:
        if MAP[x][y-1]:
            cnt,next_poss = house_count([x,y-1])
            answer.append(cnt)
            total += cnt
            q.extend(next_poss)
        else:
            total += 1
            visited[x][y-1] = True
            q.append([x,y-1])
    if y<n-1 and visited[x][y+1] == False and MAP[x][y+1]:
        if MAP[x][y+1]:
            cnt,next_poss = house_count([x,y+1])
            answer.append(cnt)
            total += cnt
            q.extend(next_poss)
        else:
            total += 1
            visited[x][y+1] = True
            q.append([x,y+1])

print(len(answer))

if answer:
    answer.sort()
    for i in answer:
        print(i)
else:
    print(0)
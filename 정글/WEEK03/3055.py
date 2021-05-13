## 탈출
## 고슴도치는 홍수를 피해 비버의 굴로 도망쳐야 한다. 도망칠 수 있을까?
## BFS
## 돌 : X, 물이 차있는 지역 : *, 비어있는 곳 : .
## 비버의 굴 : D, 고슴도치의 위치 : S
###############입력###############
import heapq
import sys
from collections import deque, defaultdict
r = sys.stdin.readline

R,C = map(int, r().split())
MAP = [list(r().strip()) for _ in range(R)]
q = deque()

time = 0
fail = "KAKTUS"

water = deque()
start = 0
end = 0
visited = [[0 for _ in range(C)] for _ in range(R)]

## 최종점에 도착했는지 여부를 판단하는 Flag
arrived = 0

for x in range(R):
    for y in range(C):
        if MAP[x][y] == '*':
            water.append([x,y])
        elif MAP[x][y] == 'S':
            start = [x,y]
            
q.append(start)
#print(q)
#for m in MAP:
#    print(m)

##################################

while q:
    
    ## 물을 먼저 채운다.
    len_w = len(water)
    for _ in range(len_w):
        x,y = water.popleft()
        
        if x>0 and MAP[x-1][y] == '.':
            if visited[x-1][y]:
                pass
            else:
                MAP[x-1][y] = '*'
                visited[x-1][y]=1
                water.append([x-1, y])
        if x<R-1 and MAP[x+1][y] == '.':
            if visited[x+1][y]:
                pass
            else:
                visited[x+1][y] = 1
                MAP[x+1][y] = '*'
                water.append([x+1,y])
        if y>0 and MAP[x][y-1] == '.':
            if visited[x][y-1]:
                pass
            else:
                visited[x][y-1] = 1
                MAP[x][y-1] = '*'
                water.append([x, y-1])
        if y<C-1 and MAP[x][y+1] == '.':
            if visited[x][y+1]:
                pass
            else:
                visited[x][y+1] = 1
                MAP[x][y+1] = '*'
                water.append([x, y+1])
    
    ## 고슴도치를 이동시킨다.
    len_q = len(q)
    
    for _ in range(len_q):
        x,y = q.popleft()

        if x>0:
            if MAP[x-1][y] == '.' and not visited[x-1][y]:
                q.append([x-1, y])
                visited[x-1][y] = 1
            elif MAP[x-1][y] == 'D':
                arrived = 1
                break
            
        if x<R-1:
            if MAP[x+1][y] == '.' and not visited[x+1][y]:
                q.append([x+1,y])
                visited[x+1][y] = 1
            elif MAP[x+1][y] == 'D':
                arrived = 1
                break
            
        if y>0:
            if MAP[x][y-1] == '.' and not visited[x][y-1]:
                q.append([x, y-1])
                visited[x][y-1] = 1
            elif MAP[x][y-1] == 'D':
                arrived = 1
                break
            
        if y<C-1:
            if MAP[x][y+1] == '.' and not visited[x][y+1]:
                q.append([x, y+1])
                visited[x][y+1] = 1
            elif MAP[x][y+1] == 'D':
                arrived = 1
                break
            
        #print(f"end : {end}, [x,y] = [{x},{y}]")
        #print(q)
        
    time += 1
    if arrived:
        #print(f"arrived, time : {time}")
        break
    #print(f"Time : {time}")
    #for m in MAP:
        #print(m)


if arrived:
    print(time)
else:
    print(fail)
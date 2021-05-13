## 토마토
## M,N,H 행렬이 주어질 때, 토마토가 전부 익을 때까지 걸리는 일수를 구하라. 불가능하면 -1을 반환하라.
## BFS
## 토마토 개수와 최종적으로 익은 토마토 개수를 비교

###############입력###############
import heapq
import sys
from collections import deque, defaultdict
r = sys.stdin.readline

m, n, h = map(int, r().split())
tomato_list = [[list(map(int, r().split())) for _ in range(n)]for _ in range(h)]
q = deque([])

## 전체 토마토 개수
tomato_num = n*m*h

## 익은 토마토 개수
done_count = 0

## 지난 날
day = -1

for i in range(len(tomato_list)):
    for j in range(len(tomato_list[i])):
        for k in range(len(tomato_list[i][j])):
            if tomato_list[i][j][k] == 1:
                q.append([i,j,k])
                done_count += 1
            elif tomato_list[i][j][k] == -1:
                tomato_num -= 1

#print(tomato_num)
#print(done_count)
##################################

while q:
    q_size = len(q)
    for _ in range(q_size):
        z, x, y = q.popleft()
        if x > 0 and tomato_list[z][x-1][y] == 0:
            tomato_list[z][x-1][y] = 1
            q.append([z, x-1, y])
            done_count += 1
        if y > 0 and tomato_list[z][x][y-1] == 0:
            tomato_list[z][x][y-1] = 1
            q.append([z, x, y-1])
            done_count += 1
        if x < n-1 and tomato_list[z][x+1][y] == 0:
            tomato_list[z][x+1][y] = 1
            q.append([z, x+1, y])
            done_count += 1
        if y < m-1 and tomato_list[z][x][y+1] == 0:
            tomato_list[z][x][y+1] = 1
            q.append([z, x, y+1])
            done_count += 1
        if z > 0 and tomato_list[z-1][x][y] == 0:
            tomato_list[z-1][x][y] = 1
            q.append([z-1, x, y])
            done_count += 1
        if z < h-1 and tomato_list[z+1][x][y] == 0:
            tomato_list[z+1][x][y] = 1
            q.append([z+1, x, y])
            done_count += 1    
    day += 1

if done_count < tomato_num:
    print(-1)
else:
    print(day)

#print(f"총 토마토 개수 : {tomato_num}, 익은 토마토 개수 : {done_count}")
#print(f"총 걸린 날 : {day}")

            

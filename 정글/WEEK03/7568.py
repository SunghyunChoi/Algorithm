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

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while q:
    q_size = len(q)
    for _ in range(q_size):
        now_z, now_x, now_y = q.popleft()
        for i in range(6):
            next_x = now_x + dx[i]
            next_y = now_y + dy[i]
            next_z = now_z + dz[i]
            if next_x <0 or next_x >=n or next_y<0 or next_y>=m or next_z <0 or next_z >= h:
                continue
            if tomato_list[next_z][next_x][next_y]:
                continue
            q.append([next_z, next_x, next_y])
            tomato_list[next_z][next_x][next_y] = 1
            done_count += 1
    day += 1

if done_count < tomato_num:
    print(-1)
else:
    print(day)

#print(f"총 토마토 개수 : {tomato_num}, 익은 토마토 개수 : {done_count}")
#print(f"총 걸린 날 : {day}")

            

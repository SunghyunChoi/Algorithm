## 알파벳
## 말이 지날 수 있는 최대 칸의 갯수를 구하라
## 각 지점에 끝에 이르면 answer에 답을 추가한다.
## answer에서 최댓값을 출력한다.

import heapq
import sys
from collections import deque, defaultdict
r = sys.stdin.readline
# 아스키코드로 업데이트
R,C = map(int, r().split())
MAP = [list(r().strip()) for _ in range(R)]
visit = defaultdict(bool)
visit[MAP[0][0]] = True
direction = [[-1,0],[1,0],[0,-1],[0,1]]
start = [0,0]
answer = 0
         
def max_path(x, y, cnt):
    global answer
    answer = max(answer, cnt)
    
    if x > 0 and visit[MAP[x-1][y]] == False:
        visit[MAP[x-1][y]] = True
        max_path(x-1, y, cnt+1)
        visit[MAP[x-1][y]] = False

    if x < R-1 and visit[MAP[x+1][y]] == False:
 
        visit[MAP[x+1][y]] = True
        max_path(x+1, y, cnt+1)
        visit[MAP[x+1][y]] = False

    if y > 0 and visit[MAP[x][y-1]] == False:
        visit[MAP[x][y-1]] = True
        max_path(x, y-1, cnt+1)
        visit[MAP[x][y-1]] = False

    if y < C-1 and visit[MAP[x][y+1]] == False:
     
        visit[MAP[x][y+1]] = True
        max_path(x, y+1, cnt+1)
        visit[MAP[x][y+1]] = False

max_path(0,0,1)
print(answer)
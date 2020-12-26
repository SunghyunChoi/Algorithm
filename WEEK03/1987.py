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
    
    for dr in direction:
        np = [x + dr[0], y + dr[1]]
        if np[0] < 0 or np[1] < 0 or np[0]>=R or np[1] >= C:
            continue

        if visit[MAP[np[0]][np[1]]]:
            continue
        
        visit[MAP[np[0]][np[1]]] = True
        max_path(np[0], np[1], cnt+1)
        visit[MAP[np[0]][np[1]]] = False


max_path(0,0,1)
print(answer)
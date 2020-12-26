## 미로탐색
## N,M 행렬이 주어질 때, [N,M]까지 도착하는 최소 거리를 구하여라.
## BFS

###############입력###############
import heapq
import sys
from collections import deque, defaultdict
r = sys.stdin.readline

n,m = map(int, r().split())
maze = [list(map(int, list(r().strip()))) for _ in range(n)]
route = [[0 for _ in range(m)] for _ in range(n)]

n -= 1
m -= 1
direction = [[-1,0],[1,0],[0,-1],[0,1]]

##################################

def find_path(arr, end):
    visited = defaultdict(bool)
    d = 0
    dq = deque([[0,0]])
    route[0][0] = 1
    while dq:
        cur = dq.popleft()
        for dr in direction:
            next_poss = [dr[0]+cur[0], dr[1]+cur[1]]
            if next_poss[0]<0 or next_poss[0]>len(arr)-1:
                continue
            elif next_poss[1]<0 or next_poss[1]>len(arr[0])-1:
                continue
            if (arr[next_poss[0]][next_poss[1]] == 1) and (visited[(next_poss[0],next_poss[1])] == False):
                dq.append(next_poss)
                visited[(next_poss[0],next_poss[1])] = True
                route[next_poss[0]][next_poss[1]] = route[cur[0]][cur[1]] + 1
                #if next_poss == end:
                #    return route[next_poss[0]][next_poss[1]]
                

find_path(maze, [n,m])
print(route[n][m])


## 미로탐색
## N,M 행렬이 주어질 때, [N,M]까지 도착하는 최소 거리를 구하여라.

###############입력###############
import heapq
import sys
from collections import deque, defaultdict
r = sys.stdin.readline

n,m = map(int, r().split())
maze = [list(map(int, list(r().strip()))) for _ in range(n)]
n -= 1
m -= 1
##################################

def find_path(arr, end):
    visited = defaultdict(bool)
    d = 0
    dq = deque([0,0])
    
    

#print(find_path(maze, [n,m]))


# def find_path(arr, end):
#     visited = defaultdict(bool)
#     visited[(0,0)] = True
#     def go(arr, end, visited, cur, d):
#         if cur == end:
#             return d
#         answer = 0
#         direction = [[-1,0],[1,0],[0,-1],[0,1]]
#         poss_list = []
#         for dr in direction:
#             next_poss = [dr[0]+cur[0], dr[1]+cur[1]]
#             if next_poss[0]<0 or next_poss[0]>len(arr)-1:
#                 continue
#             elif next_poss[1]<0 or next_poss[1]>len(arr[0])-1:
#                 continue
#             if (arr[next_poss[0]][next_poss[1]] == 1) and (visited[(next_poss[0],next_poss[1])] == False):
#                 poss_list.append(next_poss)
            
#         for n_pos in poss_list:
#             visited[(n_pos[0],n_pos[1])] = True
#             answer = go(arr, end, visited, n_pos, d+1)
#             visited[(n_pos[0]),(n_pos[1])] = False
#         return answer
#     answer = go(maze, end, visited, [0,0], 0)

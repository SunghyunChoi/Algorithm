## 바이러스
## 바이러스에 걸리는 컴퓨터의 개수를 구하라.

import heapq
import sys
from collections import deque, defaultdict
r = sys.stdin.readline

###############입력###############

v = int(r())
e = int(r())
v_list = defaultdict(list)

for i in range(e):
    start,end = map(int, r().split())
    v_list[start].append(end)
    v_list[end].append(start)


##################################

def bfs(arr, start):
    visited = defaultdict(bool)
    answer = []
    d = deque([start])
    visited[start] = True
    while d:
        x = d.popleft()
        answer.append(x) 
        for next in v_list[x]:
            if visited[next] == False:
                d.append(next)
                visited[next] = True
    return answer

print(len(bfs(v_list, 1))-1)
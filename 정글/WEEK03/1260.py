## DFS와 BFS
## 인접 리스트로 구현해보기

import heapq
import sys
from collections import deque, defaultdict

r = sys.stdin.readline

###############입력###############

v, e, s = map(int, r().split()) ## Vertice, Edge, Start
v_list = [[] for _ in range(v+1)] ## 표현이 편하게 0번째 배열은 비워놓는다.

for i in range(e):
    start, end = map(int, r().split())
    v_list[start].append(end) # 두번 방문할 가능성이 없으므로 검사할 필요 없음, 중복된 요소는 들어감
    v_list[end].append(start)

for i in v_list:
    i.sort()

##################################

############ 함수 선언 ############

## BFS(너비우선탐색) 순으로 출력
def bfs(arr, start):
    visited = defaultdict(bool)
    deq = deque([start])
    answer = []
    visited[start] = True
    while deq:
        x = deq.popleft()
        answer.append(x)
        for i in v_list[x]:
            if visited[i] == False:
                visited[i] = True
                deq.append(i)
    return answer

## DFS(깊이우선탐색) 순으로 출력
def dfs(arr, start):
    visited = defaultdict(bool)
    stk = [start]
    answer = []
    while stk:
        x = stk.pop()
        if visited[x] == False:
            visited[x] = True
            answer.append(x)
            stk.extend(v_list[x][::-1])
    return answer

###############실행################

print(*dfs(v_list, s))
print(*bfs(v_list, s))

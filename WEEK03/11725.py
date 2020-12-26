## 트리의 부모 찾기
## 리스트의 연결 정보가 주어질 때, 부모 정보를 순차적으로 출력하라.
## DFS
import heapq
import sys
from collections import deque, defaultdict
r = sys.stdin.readline

n = int(r())
graph_list = [[] for _ in range(n+1)]
parent_list = [0 for _ in range(n+1)]
for _ in range(n-1):
    start,end = map(int, r().split())
    graph_list[start].append(end)
    graph_list[end].append(start)


start = 1
q = deque([1])

while q:
    x = q.popleft()
    for i in graph_list[x]:
        if parent_list[i]:
            continue
        parent_list[i] = x
        q.append(i)

print('\n'.join(map(str, parent_list[2:])))
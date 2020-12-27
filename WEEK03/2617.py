## 구슬 찾기
## N개의 구슬에 대해서 M쌍의 대소비교 결과가 주어진다.
## (N+1)/2번째 구슬이 될 수 없는 구슬의 개수를 구하라.
## bfs를 사용하여 level 별 개수를 파악한다. 마지막 level과 맨 위 level

####################  입력  ####################
import heapq
import sys
from collections import deque, defaultdict
r = sys.stdin.readline

n,m = map(int, r().split())
c_tree = [[] for _ in range(n+1)]
p_tree = [[] for _ in range(n+1)]
cmpr = []
for i in range(m):
    p, c = map(int, r().split())
    c_tree[p].append(c)
    p_tree[c].append(p)
answer = 0
parent = [0 for _ in range(n+1)]
child = [0 for _ in range(n+1)]
bk = False
################################################

for i in range(1, n+1):
    stk = [i]
    bk = False
    visited = [False for _ in range(n+1)]
    ## 자식 노드의 개수 찾기
    while stk:
        x = stk.pop()
        for k in c_tree[x]:
            if visited[k] ==True:
                continue
            else:
                child[i] += 1
                visited[k] = True
                stk.append(k)
            if child[i] > n//2:
                answer += 1
                bk = True
                break    
        if bk == True:
            break
    if bk == True:
        continue
    ## 부모 노드의 개수 찾기
    stk = [i]
    visited = [False for _ in range(n+1)]
    while stk:
        x = stk.pop()
        for k in p_tree[x]:
            if visited[k] == True:
                continue
            else:
                parent[i] += 1
                visited[k] = True
                stk.append(k)
            if parent[i] > n//2:
                answer += 1
                bk = True
                break
        if bk == True:
            break
        
print(answer)

#print(answer)
#print(parent)
#print(child)
#print(p_tree)
#print(c_tree)

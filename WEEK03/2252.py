## 줄 세우기
## 학생 수 : N, 비교 횟수 : N
## 순서를 구하라
## 위상 정렬

####################  입력  ####################
import heapq
import sys
from collections import deque, defaultdict
r = sys.stdin.readline

answer = []
n,m = map(int, r().split())
num_e = [0 for i in range(n+1)]
list_e = [[] for i in range(n+1)]

for i in range(m):
    s, e = map(int, r().split())
    list_e[s].append(e)
    num_e[e] += 1

q = deque()

while True:
    for i in range(1, n+1):
        if num_e[i] == 0:
            q.append(i)
    for i in range(1,n+1):
        x = q.popleft()
        answer.append(x)
        for j in list_e[x]:
            num_e[j] -= 1
            if num_e[j] == 0:
                q.append(j)
    if not q:
        break
print(*answer)
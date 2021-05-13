## 숨바꼭질 : 동생을 찾아라
## 1차원
## bfs하면서 전체 위치 탐색

####################  입력  ####################
import heapq
import sys
from collections import deque, defaultdict
r = sys.stdin.readline
start,end = map(int,r().split())
total = 1
minimum = [-1 for _ in range(100001)]
answer = []
#################################################

q = deque([start])
minimum[start] = 0

while q:
    x = q.popleft()
    #print(x, minimum[x])
    if x>0 and minimum[x-1] == -1:
        minimum[x-1] = minimum[x]+1
        q.append(x-1)
        if x-1 == end:
            break
    if x>end:
        continue
    if x<100000 and minimum[x+1] == -1:
        minimum[x+1] = minimum[x]+1
        q.append(x+1)
        if x+1 == end:
            break
    if x<=50000 and minimum[2*x] == -1:
        minimum[2*x] = minimum[x] + 1
        q.append(2*x)
        if 2*x == end:
            break

if start==end:
    print(0)
else:
    print(minimum[end])


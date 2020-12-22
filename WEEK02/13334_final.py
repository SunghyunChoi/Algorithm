##철로
## [시작점, 끝점]들이 주어지고 길이 d의 직선이주어질 때
## 임의의 위치에 직선을 놓았을 때 포함되는 [시작점,끝점] 의 최댓값을 구하시오.

import sys
import heapq
from operator import itemgetter
r = sys.stdin.readline

n = int(r())
lines = list(sorted(map(int, r().split())) for _ in range(n))
lines = sorted(lines, key = itemgetter(1))
#print(lines)
d = int(r())
answer = 0
heap = []

for i in range(len(lines)):
    left = lines[i][0]
    right = lines[i][1]

    heapq.heappush(heap, left)

    while len(heap)>0 and heap[0] < right - d:
        heapq.heappop(heap)
    answer = max(answer, len(heap))

print(answer)

    
    


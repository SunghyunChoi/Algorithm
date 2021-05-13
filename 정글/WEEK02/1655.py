## 가운데를 말해요

import heapq
import sys
from collections import deque
r = sys.stdin.readline

n = int(r())
heap = []
heap_mid = []
left = 0
right = 0
mid = 0
mid_val = 0

for _ in range(n):
    heapq.heappush(heap, int(r()))
    
    mid = (left + right) // 2
    
    while len(heap_mid) < mid + 1:
        heapq.heappush(heap_mid, -1 * heapq.heappop(heap))

    mid_val = -1 * heapq.heappop(heap_mid)
    print(mid_val)

    heapq.heappush(heap, mid_val)
    right += 1
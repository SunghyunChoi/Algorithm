import sys
import heapq
from collections import deque
r = sys.stdin.readline

heap = []

n = int(r())

for _ in range(n):
    cmd = int(r())

    if cmd :
        heapq.heappush(heap, -1 * cmd)
    else :
        try:
            print(-1 * heapq.heappop(heap))
        except:
            print(0)
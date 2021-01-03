## 동전 0

####################  입력  ####################
import heapq
import sys
from collections import deque, defaultdict
r = sys.stdin.readline
#################################################

n,k = map(int, r().strip().split())
coins = [int(r()) for _ in range(n)]
count = 0
result = k

for i in range(n-1, -1, -1):
    count += k // coins[i]
    k = k % coins[i]
    if k == 0:
        break

print(count)
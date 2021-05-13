## 피보나치

####################  입력  ####################
import heapq
import sys
from collections import deque, defaultdict
r = sys.stdin.readline

#################################################

n = int(r())
i = 2
f = [0 for _ in range(n+1)]
f[0] = 0
f[1] = 1

while i<=n:
    f[i] = f[i-1] + f[i-2]
    i += 1

print(f[n])
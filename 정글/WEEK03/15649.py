## n과m (1)
## 순열을 구하라

####################  입력  ####################
import heapq
import sys
from collections import deque, defaultdict
r = sys.stdin.readline

n,m = map(int, r().split())
arr = []
visited = [False for _ in range(n+1)]
val = set()
################################################

def permutate(cnt, m):
    if cnt == m:
        if arr not in val:
            print(*arr)
            val.add(arr)
    else:
        for i in range(1, n+1):
            if not visited[i]:
                visited[i] = True
                arr.append(i)
                permutate(cnt+1, m)
                visited[i] = False
                arr.pop()

permutate(0, m)

## 01타일

####################  입력  ####################
import heapq
import sys
from collections import deque, defaultdict
r = sys.stdin.readline

#################################################

N = int(r())
until_N = 3
answer = [0 for _ in range(N)]

while until_N<=N:
    answer.append((answer[-1] + answer[-2])%15746)
    until_N += 1

print(answer[N])
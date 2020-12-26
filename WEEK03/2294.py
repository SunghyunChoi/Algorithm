## 동전2
## n개의 동전이 주어질 때, 동전 개수를 최소로 하여 k원을 지불하라. 이 때 동전 개수를 반환하라.
## BFS

import heapq
import sys
from collections import deque, defaultdict
r = sys.stdin.readline

n,k = map(int, r().split())
coin = []
for i in range(n):
    coin.append(int(r()))
coin = sorted(coin, reverse = True)
cnt = 1
##집합을 사용하여 특정 가격 조합까지 도달하는 최소거리를 계산한다.
visit = set(coin)
q = deque(coin)

finish = False
while q:
    len_q = len(q)
    for _ in range(len_q):
        now = q.popleft()
        for i in coin:
            n_now = now + i
            if n_now >k:
                continue
            elif n_now in visit:
                continue
            else:
                visit.add(n_now)
                q.append(n_now)
            if n_now == k:
                finish = True
                break
        if finish:
            break
    cnt += 1
    if finish:
        break

if finish:
    print(cnt)
else:
    print(-1)

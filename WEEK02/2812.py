## 크게 만들기
## N자리 숫자가 주어질 때, K개의 수를 지운 수 중 가장 큰 수를 찾아라.

import heapq
import sys
from collections import deque
r = sys.stdin.readline

n,k = map(int, r().split())
num = list(map(int, list(r().strip())))

stk = deque([])

for i in range(k):
    x = num[i]
    #print(x)
    if not stk:
        stk.append(x)
    else:
        while stk:
            if stk[-1] < x:
                stk.pop()
            else:
                break
        stk.append(x)
#print(stk, num[k:])

for i in range(k, n):
    x = num[i]
    if not stk:
        stk.append(x)
    else:
        while stk:
            if stk[-1] < x:
                stk.pop()
            else:
                break
        stk.append(x)
    print(stk.popleft(), end='')
## 히스토그램에서 가장 큰 직사각형
import heapq
import sys
from collections import deque
r = sys.stdin.readline

a = 'start'


while True:
    a = list(map(int, r().split()))
    if a == [0]:
        break
    n = a[0]
    stk = []
    answer = 0

    for i in range(1, n+1):
        c_h = [a[i], i] # Current Height
        if not stk:
            stk.append([a[i], i])
        else:
            while stk:
                stk_peek = stk[-1]
                if stk_peek[0] > c_h[0]:
                    answer = max(answer, (stk_peek[0]) * (i - stk_peek[1]))
                    stk.pop()
                    c_h[1] = stk_peek[1]
                    if not stk:
                        stk.append(c_h)
                        break
                elif stk_peek[0] < c_h[0]:
                    stk.append(c_h)
                    break
                else:
                    break
    
    x = n+1
    for i in stk:
        answer = max(answer, (x-i[1]) * i[0])
    print(answer)
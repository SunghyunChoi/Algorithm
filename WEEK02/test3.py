## 소수의 곱

import sys
from collections import deque
import heapq

r = sys.stdin.readline

###########     입력     ###########

n, find_num = map(int, r().split())
num_list = list(map(int, r().split()))
heapq.heapify(num_list)
answer = []
####################################

while len(answer)-1 < find_num:
    start = num_list[0]
    x = len(num_list)
    for i in range(x):
        heapq.heappush(num_list, num_list[i] * start)
    answer.append(heapq.heappop(num_list))

print(answer)

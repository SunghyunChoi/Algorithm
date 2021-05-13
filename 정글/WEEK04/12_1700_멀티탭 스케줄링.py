## 멀티탭 스케쥴링
## 플러그를 뽑는 횟수를 최소화하라.

import sys
from collections import Counter, deque
r = input#sys.stdin.readline

## 풀이 1. 가장 많이 사용하는 순서대로 나열한다.


def time_pass(arr):
    for i in range(len(arr)):
        arr[i][1] -= 1

tap_num, use_count = map(int, r().split())
use_case = list(map(int, r().split()))
taps = set()
count = Counter(use_case)
answer = 0

for i in range(tap_num):
    try:
        next_use = use_case.pop(0)
        count[next_use] -= 1
        taps.add(next_use)
    except:
        break
#print(taps)
while use_case:
    next_use = use_case.pop(0)
    if next_use in taps:
        count[next_use] -= 1
    elif len(taps)<tap_num:
        taps.add(next_use)
        count[next_use] -= 1
    else:
        min_num = 0
        min_use = 0
        for in_use in taps:
            if count[in_use] <= 0:
                min_use = count[in_use]
                min_num = in_use
                break
            if use_case.index(in_use) >= min_use:
                min_use = use_case.index(in_use)
                min_num = in_use
                
        taps.remove(min_num)
        taps.add(next_use)
        #print(f"pop {min_num}, {taps}")
        answer += 1
        count[next_use] -= 1
    
print(answer)
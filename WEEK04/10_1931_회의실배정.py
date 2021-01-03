##회의실 배정

####################  입력  ####################
import heapq
import sys
from collections import deque, defaultdict
r = sys.stdin.readline
#################################################

n = int(r())
start_end = [list(map(int, r().split())) for _ in range(n)]
start_end.sort(key = lambda x: x[0])
#print(n, start_end)
answer = [start_end[0]]
for i in range(1, len(start_end)):
    compare = answer[-1]
    compare_with = start_end[i]
    if compare[1] > compare_with[1]:
        answer[-1] = compare_with
    else:
        if compare_with[0] >= compare[1]:
            answer.append(compare_with)
    #print(answer)

print(len(answer))
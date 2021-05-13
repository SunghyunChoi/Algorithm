## 카드 정렬하기
## N개의 숫자 카드 묶음의 크기를 하나로 합칠 때, 필요한 최소 비교 횟수를 구하시오.

import sys
import heapq
r = sys.stdin.readline

n = int(r())
heap = [10, 10, 20, 20, 20]#heapq.heapify(list(map(int, sys.stdin.read().split())))
heapq.heapify(heap)
#print(heap)
start = 0
compare = 0
answer = 0

while len(heap) > 1:
    start = heapq.heappop(heap)
    compare = heapq.heappop(heap)
    answer += (start + compare)
    heapq.heappush(heap, start + compare)
    #print(heap)
print(answer)
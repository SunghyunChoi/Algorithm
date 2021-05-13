##철로
## [시작점, 끝점]들이 주어지고 길이 d의 직선이주어질 때
## 임의의 위치에 직선을 놓았을 때 포함되는 [시작점,끝점] 의 최댓값을 구하시오.

import sys
import heapq
from operator import itemgetter
r = sys.stdin.readline

n = int(r())
heap = sorted(list(sorted(map(int, r().split())) for _ in range(n)), key = itemgetter(0,1))
#print(heap)
d = int(r())
answer = 0

for i in range(len(heap)):
    
    pos = heap[i]
    
    # 첫 점의 시작과 끝
    pos_start = pos[0]
    pos_end = pos[1]
    
    # 첫 점 기준으로 직선을 봤을 때 시작과 끝
    d_start = pos_start
    d_end = d_start + d

    pop_list = []
    loop_ans = 1 # loop를 돌면서 가능성 있는 정답 후보

    if d_end < pos_end:
        continue
    else:
        for j in range(i+1, len(heap)):
            x = heap[j]
            if x[0] < d_end: # 꺼낸 점의 시작점이 직선의 끝점보다 앞에 있을 때
                if x[1] <= d_end:
                    loop_ans += 1 # 꺼낸 점의 끝점이 직선의 끝점보다 앞에 있으면 loop_ans += 1
                else:
                    continue
            else:
                answer = max(answer, loop_ans)
                break

    if answer > len(heap):
        break

print(answer)

    
    


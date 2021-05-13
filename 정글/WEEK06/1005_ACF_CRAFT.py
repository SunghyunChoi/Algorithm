import sys
from collections import deque
r = sys.stdin.readline

testcase = int(r())
answer_list = []
for _ in range(testcase):
    building_num, building_order_num = map(int, r().split())
    building_time = [0] + list(map(int, r().split()))
    build_ready = [0 for _ in range(building_num+1)]
    build_ready[0] = 1
    building_order = [[] for _ in range(building_num + 1)]
    min_time = [0 for _ in range(building_num+1)]
    for _ in range(building_order_num):
        start, end = map(int, r().split())
        build_ready[end] += 1
        building_order[start].append(end)
    
    build_target = int(r())
    
    queue = deque([])
    for i in range(building_num + 1):
        if build_ready[i] == 0:
            queue.append(i)
            min_time[i] = building_time[i]
    while(queue):
        len_q = len(queue)
        max_time = 0
        for _ in range(len_q):
            build = queue.popleft()
            for next_available in building_order[build]:
                build_ready[next_available] -= 1 
                min_time[next_available] = max(min_time[next_available], min_time[build] + building_time[next_available])
                if build_ready[next_available] == 0:
                    queue.append(next_available)
        if build_ready[build_target]==0:
            queue = []
            break
    answer_list.append(min_time[build_target])


for answer in answer_list:
    print(answer)
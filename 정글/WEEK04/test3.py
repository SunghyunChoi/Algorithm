##보석도둑
####################  입력  ####################
import sys
from collections import deque, defaultdict
import heapq

r = sys.stdin.readline

gem_num, bag_num = map(int, input().split())
gem = [list(map(int, r().split())) for _ in range(gem_num)]
bag = [int(r()) for _ in range(bag_num)]

################################################

gem = sorted(gem, reverse=True)
bag = sorted(bag, reverse=True)
available_gem = []
answer = 0
#print(gem)
#print(bag)

while(bag):
    bag_to_pack = bag.pop()
    if gem:
        while (gem[-1])[0] <= bag_to_pack:
            poss_gem = gem.pop()
            heapq.heappush(available_gem, -1*poss_gem[1])
            if not gem:
                break
    if available_gem:
        answer += -1 * heapq.heappop(available_gem)
print(answer)
    
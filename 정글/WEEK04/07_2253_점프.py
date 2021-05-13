## 점프
####################  입력  ####################
import sys
from collections import deque, defaultdict
r = sys.stdin.readline
stone_num, s_stone_num = map(int, r().split())
s_stone = defaultdict(bool)
for _ in range(s_stone_num):
    s_stone[int(r())] = True
dp = [[float('inf') for _ in range(int((2*stone_num)**(0.5))+2)] for _ in range((stone_num+1))]
#################################################

def solve():
    dp[1][0] = 0
    for pos in range(2, stone_num+1):
        if not s_stone[pos]:
            for v in range(1, int((2*pos)**(0.5))+1):
                
                dp[pos][v] = min(dp[pos-v][v], dp[pos-v][v-1], dp[pos-v][v+1])+1

    answer = min(dp[stone_num])
    if answer == float('inf'):
        print(-1)
    else:
        print(answer)

solve()
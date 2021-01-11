##계단오르기
####################  입력  ####################
import sys
from collections import deque, defaultdict
r = sys.stdin.readline
x,y = map(int, r().split())
MAP = [list(map(int, r().split())) for _ in range(x)]
dp = defaultdict(int)
sys.setrecursionlimit(10000)

def dfs(_x,_y):
    if [_x,_y] == [x-1,y-1]:
        return 1
    elif dp[(_x,_y)] == -1:
        return 0
    elif dp[(_x,_y)] != 0:
        return dp[(_x,_y)]
    
    
    poss_path =0 
    #위
    if _x>0 and MAP[_x-1][_y] < MAP[_x][_y]:
        poss_path += dfs(_x-1, _y)
    #아래
    if _x<x-1 and MAP[_x+1][_y] < MAP[_x][_y]:
        poss_path += dfs(_x+1, _y)
    #왼쪽
    if _y>0 and MAP[_x][_y-1] < MAP[_x][_y]:
        poss_path += dfs(_x, _y-1)
    #오른쪽
    if _y<y-1 and MAP[_x][_y+1] < MAP[_x][_y]:
        poss_path += dfs(_x, _y+1)
    if poss_path==0:
        dp[(_x,_y)]=-1
        return 0
    dp[(_x,_y)] = poss_path
    return poss_path

dfs(0,0)

if x == 1 and y == 1:
    print(1)
elif dp[(0,0)] == -1:
    print(0)
else:
    print(dp[(0,0)])
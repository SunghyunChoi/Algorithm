## 행렬 곱셈 순서
####################  입력  ####################
import sys
r = sys.stdin.readline
n = int(r())
dist = [list(map(int, r().split())) for _ in range(n)]
start = 0
visited = 1
dp = [[0 for _ in range(1<<n)] for _ in range(n)]
#################################################

def dfs(cur, visited):
    if visited == (1<<n)-1:
        if not dist[cur][0]:
            return float('inf')
        else:
            return dist[cur][0]
        
    if dp[cur][visited]:
        return dp[cur][visited]

    min_dist = float('inf')
    for i in range(0, n):
        next_visited = visited | 1<<i
        if dist[cur][i] == 0:
            continue
        elif visited & 1<<i: 
            continue
        else:
            min_dist = min(min_dist, dfs(i, next_visited) + dist[cur][i])
    
    dp[cur][visited] = min_dist

    return min_dist


print(dfs(start, visited))

for i in dp:
    print(i)
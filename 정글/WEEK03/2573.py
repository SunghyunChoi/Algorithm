## 빙산
## 시작점을 기록하고, 시작점부터 끝날때까지 얼음을 녹인다.
## 녹인 얼음의 수와 남아있는 얼음의 수를 비교하고 같다면 계속 진행한다.
## DFS


####################  입력  ####################
import heapq
import sys
from collections import deque, defaultdict
r = sys.stdin.readline

n, m = map(int, r().split())
ice = []
start_x = float('inf')
end_x = 0
start_y = 0

count = 0
done_count = 0
visit = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    x = list(map(int, r().split()))
    if len(set(x)) != 1:
        for j in range(m):
            if x[j] != 0:
                count += 1
        start_x = min(start_x, i)
        end_x = max(end_x, i)
    ice.append(x)

for i in range(len(ice[start_x])):
    if ice[start_x][i] != 0:
        start_y = i
        break

#print(ice, start_x, start_y)
bk = False
stk = [[start_x, start_y]]
visit[start_x][start_y] = True
year = 0
start = [start_x, start_y]
erase = []
next_start = 0
next_count = count

################################################

while True:
    stk = [[start[0],start[1]]]
    erase = [[start[0],start[1]]]
    visit[start[0]][start[1]] = True
    while stk:
        x,y = stk.pop()
        minus = 0
        ## 위
        if x > 0 and visit[x-1][y] == False:
            if not ice[x-1][y]:
                minus += 1
            else:
                stk.append([x-1,y])
                erase.append([x-1,y])
                visit[x-1][y] = True
        ## 아래
        if x < n-1 and visit[x+1][y] == False:
            if not ice[x+1][y]:
                minus += 1
            else:
                stk.append([x+1, y])
                erase.append([x+1,y])
                visit[x+1][y] = True
        ## 왼쪽
        if y > 0 and visit[x][y-1] == False:
            if not ice[x][y-1]:
                minus += 1
            else:
                stk.append([x,y-1])
                erase.append([x,y-1])
                visit[x][y-1] = True
        ## 오른쪽
        if y < m-1 and visit[x][y+1] == False:
            if not ice[x][y+1]:
                minus += 1
            else:
                stk.append([x, y+1])
                erase.append([x,y+1])
                visit[x][y+1] = True

        if minus >= ice[x][y]:
            minus = ice[x][y]
            next_count -= 1
        else:
            start = [x,y]
        ice[x][y] -= minus
    if count != len(erase):
        bk = True
        break
    year += 1
    count = next_count
    if not count:
        break
    for i in erase:
        visit[i[0]][i[1]] = False
    
if bk:
    print(year)
else:
    print(0)
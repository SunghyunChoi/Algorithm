## 뱀
## 뱀이 이동하면서 사과를 먹는다.
## 사과의 위치, 뱀의 방향 전환 시기가 주어졌을 때, 게임이 끝나는 시간을 구하시오.
## 뱀이 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.
## 꼬리는 머리를 쫓아간다.
## 머리가 사과를 먹지 못하면 꼬리도 먹지 못한다.
import sys
from collections import deque
r = sys.stdin.readline

l = int(r()) # 보드의 크기
m = [[1 for _ in range(l)] for _ in range(l)]
a_num = int(r()) # 사과 개수
a_list = [] # 사과 리스트
for i in range(a_num):
    a_list.append(list(map(int, r().split())))

#사과를 배치한다. 사과가 배치된 곳은 2로 지정한다.
for i in a_list:
    m[i[0]-1][i[1]-1] = 2 
for i in m:
    print(i)

## 명령어 입력을 받는다.
c_num = int(r())
c_list = deque([])
for i in range(c_num):
    c_list.append(r().split())

# 상하좌우 
# 오른쪽으로 갈땐 +1, 왼쪽으로 갈땐 -1
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

snake = deque([[0,0]]) # 뱀의 위치
t = 0

x = 0
d_add = d[x] #1초가 지날때마다 d_add씩 더해준다.
command = 0
next_t = 0
bk = 0

while True:
    try:
        command = c_list.popleft()
        next_t = int(command[0])
    except:
        next_t = next_t + 10000

    while t< next_t:
        head = [snake[-1][0] + d_add[0], snake[-1][1] + d_add[1]]
        tail = [snake[0][0], snake[0][1]]
        try:
            if head[0] >= 0 and head[1] >= 0:
                next_pos = m[head[0]][head[1]]
            else:
                bk = 1
                break
        except:
            bk = 1
            break
        if not next_pos : #갈 수 없는 곳이라면
            bk = 1
            break
        elif next_pos == 2: # 사과가 있는 곳이라면
            snake.append(head)
            m[head[0]][head[1]] = 0
        else:
            snake.append(head)
            snake.popleft()
            m[tail[0]][tail[1]] = 1
            m[head[0]][head[1]] = 0
        print(t)
        for i in m:
            print(i)
        print()
        t += 1
    if bk:
        t += 1
        print(t)
        break

    direction = command[1]    
    if direction == 'D':
        x += 1
        if x>3:
            x %= 4
        d_add = d[x]
    else :
        x -= 1
        if x<0:
            x += 4
        d_add = d[x]

    print(direction, snake)







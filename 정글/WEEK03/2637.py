## 장난감 조립
## 완제품 번호 : N 메뉴얼 개수 : M
## 완제품을 만드는데 드는 기본 부품의 갯수를 구하라.
## 위상 정렬

####################  입력  ####################
import heapq
import sys
from collections import deque, defaultdict
r = sys.stdin.readline

n = int(r())
m = int(r())

comp_list = [[] for _ in range(n+1)]
e_num = [0 for _ in range(n+1)]
answer = [0 for _ in range(n+1)]

for i in range(m):
    to_make, need, need_num = map(int, r().split())
    comp_list[to_make].append([need, need_num])
    e_num[need] += 1

q = deque([[n, 1]])

while q:
    x, x_num = q.popleft()
    answer[x] = x_num + answer[x]
    for y, y_num in comp_list[x]:
        e_num[y] -= 1
        if e_num[y] == 0:
            q.append([y, answer[x] * y_num])
        else:
            answer[y] += answer[x] * y_num
    if comp_list[x]:
        answer[x] = 0


for i in range(1,n+1):
    if answer[i]:
        print(f"{i} {answer[i]}")
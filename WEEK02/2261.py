import sys
from collections import deque
from operator import itemgetter

r = sys.stdin.readline

n = int(r())
pos_list = [list(map(int, r().split())) for _ in range(n)]
pos_list.sort(key = itemgetter(0,1))
#print(pos_list)

## 왼쪽 오른쪽 나눠서 분할정복
def left_right(start,end, n):
    if start - end <=4:
        return find_min(start, end)
    mid = 0
    if (end-start)%2:
        mid = (start + end)//2 + 1
    else:
        mid = (start + end)//2

    line = (pos_list[mid])[0]
    d = min(left_right(start, mid), left_right(mid+1, end))
    
    

    
    
    if mid - start > 

## 특정 점 갯수 이하로 남았을 때는 직접 탐색
def find_min(start,end):
    answer = 20001
    for i in range(start, end):
        for j in range(i+1, end):
            a = pos_list[i]
            b = pos_list[j]
            answer = min(answer,(a[0] - b[0])**2 + (a[1] - b[1])**2)
    return answer

print(find_min(0,4))



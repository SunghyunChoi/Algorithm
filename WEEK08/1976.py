# 1717 여행 가자
# 유니온 자료구조 익히기
import sys
from collections import Counter, defaultdict
r = sys.stdin.readline

city_num = int(r())
trip_num = int(r())
routes = [list(map(int,r().split())) for _ in range(city_num)]
trips = list(map(int, r().split()))
#유니언 집합구조
parents = [-1 for _ in range(city_num)]

#유니언 함수

def find(x):
    if parents[x] <0 : 
        return x
    update_parent = find(parents[x])
    parents[x] = update_parent
    return update_parent

def merge(x, y):
    x = find(x)
    y = find(y)

    if x==y: return
    if parents[x] > parents[y]:
        parents[y] += parents[x]
        parents[x] = y
    else:
        parents[x] += parents[y]
        parents[y] = x

for i in range(city_num-1):
    for j in range(i+1, city_num):
        if routes[i][j]:
            merge(i,j)

#print(parents)
flag = True
for idx in range(len(trips)-1):
    if find(trips[idx]-1) == find(trips[idx+1]-1):
        continue
    else:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")
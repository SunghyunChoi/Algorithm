# 16562 친구비
# 유니온 자료구조 익히기
import sys
from collections import Counter, defaultdict
r = sys.stdin.readline

friend_num, rel_num, cash = map(int, r().split())
friends = [-1 for _ in range(friend_num+1)]

result = 0
made_friends = 0

friend_fee = [0] + list(map(int, r().split()))
friend_max = friend_fee.copy()


#유니언 함수

def find(x):
    if friends[x] <0 : 
        return x
    update_parent = find(friends[x])
    friends[x] = update_parent
    return update_parent

def merge(x, y):
    x = find(x)
    y = find(y)

    if x==y: return
    if friends[x] > friends[y]:
        friends[y] += friends[x]
        friends[x] = y
    else:
        friends[x] += friends[y]
        friends[y] = x

    if friend_max[x] > friend_max[y]:
        friend_max[x] = friend_max[y]
    else:
        friend_max[y] = friend_max[x]
        

for _ in range(rel_num):
    f_a, f_b = map(int, r().split())
    merge(f_a,f_b)

for i in range(1, friend_num+1):
    if friends[i] < 0:
        result += friend_max[i]
        made_friends += (-1)*friends[i]

#print(friends)

if made_friends == friend_num and result <= cash:
    print(result)
else:
    print("Oh no")
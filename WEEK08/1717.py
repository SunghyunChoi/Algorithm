# 1717 집합의 표현
# 유니온 자료구조 익히기
import sys
from collections import Counter, defaultdict
r = sys.stdin.readline

node_num, query_num = map(int, r().split())
parent = [-1 for _ in range(node_num+1)]
answer = ["NO", "YES"]
answer_list = []
def find(x):
    # parent는 자신이 root 노드인 노드에 대해서는 트리의 깊이를 음수로 저장하고 있다.
    # (ex : 트리의 높이 3인 루트 노드의 parent[i] = -3)
    if parent[x] < 0:
        return x
    update_parent = find(parent[x])
    parent[x] = update_parent
    return update_parent

def merge(x, y):
    x = find(x)
    y = find(y)

    #같은 집합에 있으면 합칠 필요가 없다.
    if x==y: return
    # 높이가 낮은 tree를 높은 tree에 갖다 붙인다.
    if parent[x] < parent[y]:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y



for _ in range(query_num):
    query, num_a, num_b = map(int, r().split())
    # query == 1 : 소속 집합이 같은지 확인해라
    if query:
        a_root = find(num_a)
        b_root = find(num_b)
        if a_root==b_root:
            answer_list.append(1)
        else:
            answer_list.append(0)

    # query == 0 : 집합을 합쳐라
    else:
        merge(num_a,num_b)

for x in answer_list:
    print(answer[x])
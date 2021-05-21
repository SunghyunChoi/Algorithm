#최단 경로
#다익스트라
import heapq
import sys
from collections import defaultdict
r = sys.stdin.readline


def solution():
    nodeNum, edgeNum = map(int, r().rstrip().split())
    startNode = int(r())
    graph = [[] for _ in range(nodeNum+1)]
    distance = [float('inf') for _ in range(nodeNum+1)]
    q = []

    for _ in range(edgeNum):
        start, end, dist = map(int, r().rstrip().split())
        graph[start].append((dist, end))

    heapq.heappush(q, (0, startNode))
    distance[startNode] = 0

    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue

        for path in graph[node]:
            cost = dist + path[0]
            if cost < distance[path[1]]:
                distance[path[1]] = cost
                heapq.heappush(q, (cost, path[1]))

    for idx in range(1, startNode):
        if distance[idx] == float('inf'):
            print('INF')
        else:
            print(distance[idx])
    
    print(0)

    for idx in range(startNode+1, len(distance)):
        if distance[idx] == float('inf'):
            print('INF')
        else:
            print(distance[idx])

if __name__=='__main__':
    solution()
    
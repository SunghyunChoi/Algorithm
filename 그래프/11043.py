#경로 찾기
#갈 수 있는 경로들을 모두 표시하라.

import sys
r = sys.stdin.readline

def solve():
    N = int(r())
    path = [list(map(int, r().strip().split())) for _ in range(N)]
    pathList = [[] for _ in range(N)]
    answer = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if path[i][j]:
                pathList[i].append(j)

    for i in range(N):
        possPath = [x for x in pathList[i]]
        pathSet = set()
        
        while possPath:
            nextPath = possPath.pop()
            if nextPath in pathSet:
                continue
            if nextPath == i:
                answer[i][i] = 1
                pathSet.add(i)
                continue
            answer[i][nextPath] = 1
            possPath.extend(pathList[nextPath])
            pathSet.add(nextPath)

    for ans in answer:
        print(*ans)

if __name__=='__main__':
    solve()
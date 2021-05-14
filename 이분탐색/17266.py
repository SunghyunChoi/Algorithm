#어두운 굴다리
#높이 H인 가로등은 양옆으로 H씩, 총 2H만큼 밝게 한다.
#굴다리의 총 길이 N, 설치 가로등 수 M, 설치 가능 위치 positions가 주어질 때, 최소 높이를 구하라.

import sys
r = sys.stdin.readline

def testHeight(N, M, H, positions):

    firstLightIdx = 0
    while firstLightIdx+1 < len(positions) and positions[firstLightIdx+1] <= H:
        firstLightIdx += 1

    firstLight = positions[firstLightIdx]
    if firstLight > H:
        return False
    lightNum = M
    curPos = firstLightIdx
    nextPos = curPos
    lastLight = positions[curPos]
    
    while lightNum>0 and curPos < len(positions)-1:
        while nextPos < len(positions)-1:
            if positions[nextPos+1] - positions[curPos] <= 2*H:
                nextPos += 1
            else:
                break
        
        if curPos == nextPos:
            return False
        lightNum-=1
        lastLight = positions[curPos]
        curPos = nextPos

    if lightNum:
        lastLight = positions[curPos]

    if N-lastLight > H:
        return False
    
    return True

def solutions(N, M, positions):
    
    left = (N//(2*M))+1 if N%(2*M) else N//(2*M)
    right = N
    answer = 0

    while left<=right:
        mid = (left+right)//2
        if testHeight(N, M, mid, positions):
            right = mid - 1
            answer = mid
        else:
            left = mid + 1

    return answer

if __name__=='__main__':

    N = int(r())
    M = int(r())
    positions = list(map(int, r().strip().split()))
    
    print(solutions(N, M, positions))
#게임

import sys
r = sys.stdin.readline

def getWinRate(winGame, totalGame):

    return winGame*100//totalGame
def solution():
    totalGame, winGame= map(int, r().rstrip().split())
    oldWinRate = getWinRate(winGame, totalGame)
    if oldWinRate >= 99:
        return -1
    answer = -1

    left = 1
    right = int((totalGame*totalGame)/(99*totalGame-100*winGame))+1
    
    while left<=right:
        mid = (left+right)//2
        
        newWinRate = getWinRate(winGame+mid, totalGame+mid)
        if oldWinRate != newWinRate:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer

if __name__=='__main__':
    answer = solution()
    print(answer)
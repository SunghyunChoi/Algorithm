#이긴 시간 구하기
#농구 시간은 48분
#각 팀이 이기고있던 시간을 구하라.
#입력형식 1 01:10
#        팀 골넣은시간

import sys
r = sys.stdin.readline

def timeElapsed(oldMinute, oldSecond, newMinute, newSecond):
    
    extra = 0
    secondElapsed = newSecond - oldSecond
    minuteElapsed = newMinute - oldMinute
    
    if secondElapsed < 0:
        extra = -1
        secondElapsed += 60
    elif secondElapsed >59:
        extra = 1
        secondElapsed -= 60

    minuteElapsed += extra
    return (minuteElapsed, secondElapsed)
    
def solution():
    goals = int(r())
    #0번째는 무시한다.
    scores = [0, 0, 0]
    winningTime = [[0,0], [0,0], [0,0]]
    winningTeam = 0
    minute = 0
    second = 0
    
    inputString = []
    for _ in range(goals):
        team, scoreTime = r().strip().split()
        team = int(team)
        scoreMinute, scoreSecond = map(int, scoreTime.split(':'))
        inputString.append((team, scoreMinute, scoreSecond))

    inputString = sorted(inputString, key=lambda x:(x[1], x[2]))

    for string in inputString:
        team, scoreMinute, scoreSecond = string
        minuteElapsed, secondElapsed = timeElapsed(minute, second, scoreMinute, scoreSecond)
        winningTime[winningTeam][0] += minuteElapsed
        winningTime[winningTeam][1] += secondElapsed
        
        scores[team] += 1
        if scores[1] > scores[2]:
            winningTeam = 1
        elif scores[2] > scores[1]:
            winningTeam = 2
        else:
            winningTeam = 0
        
        
        minute = scoreMinute
        second = scoreSecond
    
    minuteElapsed, secondElapsed = timeElapsed(minute, second, 48, 0)
    winningTime[winningTeam][0] += minuteElapsed
    winningTime[winningTeam][1] += secondElapsed

    # 분 초를 마지막에 환산해준다.
    if winningTime[1][1]>59:
        minute = winningTime[1][1]//60
        winningTime[1][0] += minute
        winningTime[1][1] -= 60*minute
    if winningTime[2][1]>59:
        minute = winningTime[2][1]//60
        winningTime[2][0] += minute
        winningTime[2][1] -= 60*minute

    for i in range(1, 3):
        for j in range(2):
            if winningTime[i][j] < 10:
                winningTime[i][j] = '0' + str(winningTime[i][j])
            else:
                winningTime[i][j] = str(winningTime[i][j])
    print(winningTime[1][0]+':'+winningTime[1][1])
    print(winningTime[2][0]+':'+winningTime[2][1])

if __name__=='__main__':
    solution()

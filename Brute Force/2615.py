#오목
import sys
from collections import deque
r = sys.stdin.readline

def testPos(board, x, y, direction):
    count = 1
    curX = x
    curY = y
    color = board[curX][curY]
    dirX = direction[0]
    dirY = direction[1]
    answerList = [(curX, curY)]

    #이전 방향에 같은 돌 존재 여부 테스트
    nextX = x - dirX
    nextY = y - dirY
    
    if 0<=nextX<19 and 0<=nextY<19:
        if board[nextX][nextY] == color:
            return False, []

    while count < 5:
        nextX = curX + dirX
        nextY = curY + dirY
        try:
            if board[nextX][nextY] == color:
                count += 1
                answerList.append((nextX,nextY))
                curX = nextX
                curY = nextY
            else:
                return False, []
        except:
            break
        
    #뒤에 같은 색의 돌이 더 남았는지 테스트
    nextX = curX + dirX
    nextY = curY + dirY
    if 0<=nextX<19 and 0<=nextY<19:
        if board[nextX][nextY] == color:
            return False, []

    answerList = sorted(answerList, key=lambda x:(x[1], x[0]))
    
    return True, answerList

def solution():
    board = [r().strip().split() for _ in range(19)]
    answer = 0
    winColor = 0

    for i in range(19):
        for j in range(19):
            if board[i][j] in ['1', '2']:
                color = board[i][j]
                directionList = []
                #오른쪽, 오른쪽아래, 아래, 왼쪽아래에 대해서만 테스트한다.

                #오른쪽
                if j<15 and board[i][j+1] == color:
                    directionList.append((0, 1))
                #아래
                if i<15 and board[i+1][j] == color:
                    directionList.append((1, 0)) 
                #오른쪽 아래
                if i<15 and j<15 and board[i+1][j+1] == color:
                    directionList.append((1, 1)) 
                #왼쪽 아래
                if i<15 and j>3 and board[i+1][j-1] == color:
                    directionList.append((1, -1))

                for direction in directionList:
                    result, answerList = testPos(board, i, j, direction)
                    if result:
                        winColor = color
                        answer = answerList[0]
                        return winColor, answer
    return 0, []

if __name__=='__main__':
    color, answer = solution()
    print(color)
    if answer:
        print(answer[0]+1, answer[1]+1, end=' ')
    
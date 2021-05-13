import sys
r = sys.stdin.readline

size = int(r())
board = [list(map(int, r().strip().split())) for _ in range(size)]
print(size, board)

jewels = []
impurities = []

for i in range(size):
    for j in range(size):
        if board[i][j] == 2:
            jewels.append([i,j])
        elif board[i][j] == 1:
            impurities.append([i,j])

print(jewels, impurities)

def solution(left, top, right, bottom, direction, jewel, impurity):
    insideJewel = []
    insideImpurity = []
    cutAble = []
    Filter = []
    answer = 0

    # 1 가로 -1 세로
    if direction == -1:
        cutAble = [0 for _ in range(right - left+1)]
        Filter = [0, 1]
    else:
        cutAble = [0 for _ in range(bottom - top+1)]
        Filter = [1, 0]

    for j in jewel:
        x = j[0]
        y = j[1]
        if top <= x <= bottom and left <= y <= right:
            insideJewel.append(j)
            cutAble[Filter[0] * x + Filter[1] * y] -= 20
    for i in impurity:
        x = i[0]
        y = i[1]
        if top <= x <= bottom and left <= y <= right:
            insideImpurity.append(i)
            cutAble[Filter[0] * x + Filter[1] * y] += 1

    if len(insideJewel) == 1 and len(insideImpurity) == 0:
        return 1

    for cut in cutAble:
        if cut > 0 and direction == 1:
            print(cut, direction)
            answer += solution(left, top, right, cut-1, direction*-1, insideJewel, insideImpurity) * solution(left, cut+1, right, bottom, direction*-1, insideJewel, insideImpurity)
        elif cut > 0 and direction == -1:
            print(cut, direction)
            answer += solution(left, top, cut-1, bottom, direction*-1, insideJewel, insideImpurity) * solution(cut+1, top, right, bottom, direction*-1, insideJewel, insideImpurity)

    return answer

answer = solution(0, 0, size, size, 1, jewels, impurities) + solution(0, 0, size, size, -1, jewels, impurities)
print(answer)
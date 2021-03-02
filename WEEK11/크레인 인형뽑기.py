def check_pop(result, next):
    if result[-1] == next:
        return 1
    else:
        return 0

def solution(board, moves):
    answer = 0
    
    cols = [[] for _ in range(len(board))]
    result = [0]
    for i in range(len(board)-1, -1, -1):
        for j in range(len(board)):
            if board[i][j]:
                cols[j].append(board[i][j])
    
    for move in moves:
        target = cols[move-1]
        if target:
            next = target.pop()
            if check_pop(result, next):
                result.pop()
                answer += 2
            else:
                result.append(next)
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))


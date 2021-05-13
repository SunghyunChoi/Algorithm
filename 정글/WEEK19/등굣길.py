def solution(m, n, puddles):
    answer = 0
    MAP = [[0 for _ in range(m+1)] for _ in range(n+1)]
    MAP[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if([j,i] in puddles):
                continue    
            MAP[i][j] = MAP[i-1][j] + MAP[i][j-1] + MAP[i][j]
    # print(MAP)
    return MAP[n][m]%1000000007

print(solution(4,3,[[2,2]]))
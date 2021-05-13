n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# computers = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]
    
    for i in range(n):
        stk = []
        if not visited[i]:
            visited[i] = 1
            stk.append(i)
            answer += 1
        while(stk):
            start = stk.pop()
            for j in range(0, n):
                if start==j:
                    continue
                if computers[start][j]==1 and visited[j]==0:
                    visited[j] = 1
                    stk.append(j)
    return answer

print(solution(n, computers))
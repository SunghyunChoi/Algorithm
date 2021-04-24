
# key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
# lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
key = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
lock = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]

import copy
def getSum(arr, n, m):
    start = m-1
    end = n+m-1
    answer = 0
    for i in range(start, end):
        for j in range(start, end):
            answer += arr[i][j]
    return answer

def setLock(window, n, m, lock):
    
    start = m-1
    end = n+m-1
    answer = 0
    for i in range(start, end):
        for j in range(start, end):
            window[i][j] = lock[i-m+1][j-n-m+1]

def setKey(window, i, j, key):
    for p in range(len(key)):
        for q in range(len(key)):
            window[i+p][j+q] = key[p][q] ^ window[i+p][j+q]

def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret

def solution(key, lock):
    answer = False
    n = len(lock)
    m = len(key)
    requiredSum = n*n
    windowSize = n + 2*m - 2
    window = [[0 for _ in range(windowSize)] for _ in range(windowSize)]

    iterSize = n + m - 1
    for rotate in range(4):
        print(key)
        for i in range(iterSize):
            for j in range(iterSize):
                setLock(window, n, m, lock)
                setKey(window, i, j, key)
                if(getSum(window, n, m) == requiredSum):
                    answer = True
                    return answer
        key = rotate_90(key)
    return answer

print(solution(key, lock))
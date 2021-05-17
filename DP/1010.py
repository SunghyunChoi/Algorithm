#다리놓기

import sys
r = sys.stdin.readline


def solution():
    testCase = int(r())

    N = []
    M = []
    for _ in range(testCase):
        n,m = map(int, r().strip().split())
        N.append(n)
        M.append(m)

    dp = [[0 for _ in range(max(M)+1)] for _ in range(max(N)+1)]

    for n,m in zip(N,M):
        for i in range(1, n+1):
            for j in range(1, m+1):
                if dp[i][j]==0:
                    if i==j:
                        dp[i][j] = 1
                    elif i==1:
                        dp[i][j] = j
                    else:
                        dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
        print(dp[i][j])

if __name__=='__main__':
    solution()
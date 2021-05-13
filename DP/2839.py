#설탕 배달
#N이 주어졌을 때, 최소한의 3과 5의 덧셈 조합으로 N을 나타내라.
#answer = 총 3과 5의 개수

import sys
r = sys.stdin.readline

N = int(r())
if N>=6:
    dp = [float('inf') for _ in range(N+1)]
else:
    dp = [float('inf') for _ in range(6)]

dp[3], dp[5] = 1, 1
for i in range(6, N+1):
    dp[i] = min(dp[i-3]+1, dp[i-5]+1)

if(dp[N]==float('inf')):
    print(-1)
else:
    print(dp[N])
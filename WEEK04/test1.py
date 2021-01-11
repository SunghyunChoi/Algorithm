## 행렬 곱셈 순서
####################  입력  ####################
import sys
r = sys.stdin.readline

step_num = int(r())
step = [0]
for _ in range(step_num):
    step.append(int(r()))
dp = [0 for _ in range(step_num+1)]
dp[0] = step[0]
dp[1] = step[1]
#################################################

for i in range(2, step_num + 1):
    
    dp[i] = max(step[i-1]+dp[i-3], dp[i-2]) + step[i]

#print(step)
print(dp[-1])
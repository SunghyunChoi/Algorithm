## 행렬 곱셈 순서
####################  입력  ####################
import sys
r = sys.stdin.readline
#################################################

arr_num = int(r())
d0, d1 = map(int, r().split())
arr = [d0,d1]
for _ in range(arr_num-1):
    _, dx = map(int, r().split())
    arr.append(dx)
dp = [[0 for _ in range(arr_num+1)] for _ in range(arr_num+1)]

def get(x,y):
    minimum = float('inf')
    
    for i in range(x,y):
        minimum = min(minimum, dp[x][i] + dp[i+1][y] + arr[x-1] * arr[i] * arr[y])

    return minimum

for i in range(2, arr_num+1):
    start_x = 1
    start_y = i
    for j in range(0, arr_num-i+1):
        dp[start_x+j][start_y+j] = get(start_x+j, start_y+j)

print(dp[1][arr_num])
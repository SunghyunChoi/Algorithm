## 평범한 배낭
## W의 무게를 가진 배낭에 N개의 물건들 중 일부를 골라 넣으려고 한다.
## 각각 물건은 다른 가치를 가질 때, 가방이 가질 수 있는 가치의 최댓값을 찾아라.

####################  입력  ####################
import sys
r = sys.stdin.readline
#################################################

product_num, max_weight = map(int, r().split())
dp = [[0 for _ in range(max_weight+1)] for _ in range(product_num+1)]
product_weight = [0]
product_value = [0]

for _ in range(product_num):
    weight, value = map(int, r().split())
    product_weight.append(weight)
    product_value.append(value)


for i in range(1, product_num+1):
    for j in range(1, max_weight+1):
        # j represents the current possible weight
        if product_weight[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-product_weight[i]] + product_value[i])

print(dp[product_num][max_weight])
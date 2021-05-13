## LCS : Longest Common Subsequence(최장공통부분수열)
## 두 문자열이 주어질 때, 최장 공통 부분수열을 구하라.

####################  입력  ####################
import sys
r = sys.stdin.readline
#################################################

str_a = list(r().strip())
str_b = list(r().strip())

n = len(str_a)
m = len(str_b)

lcs_arr = [[0 for _ in range(n+1)] for _ in range(m+1)]

for i in range(1, m+1):
    for j in range(1, n+1):
        if str_b[i-1] == str_a[j-1]:
            lcs_arr[i][j] = lcs_arr[i-1][j-1] + 1
        else:
            lcs_arr[i][j] = max(lcs_arr[i-1][j], lcs_arr[i][j-1])

print(lcs_arr[m][n])
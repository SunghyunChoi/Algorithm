#DP
import sys
r = sys.stdin.readline

length = int(r())
tri = [list(map(int, r().strip().split())) for _ in range(length)]
answer = [[0]*(i+1) for i in range(length)]

answer[0][0] = tri[0][0]
print(answer)
for i in range(1, length):
    answer[i][0] = answer[i-1][0] + tri[i][0]
    for j in range(1, len(answer[i])-1):
        # print(i, j)
        answer[i][j] = max(answer[i-1][j], answer[i-1][j-1]) + tri[i][j]
    answer[i][-1] = answer[i-1][-1] + tri[i][-1]

print(max(answer[-1]))
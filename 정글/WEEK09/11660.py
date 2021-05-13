#구간 합 구하기 5
import sys
r = sys.stdin.readline

num, add_num = map(int, r().split())
numbers = [[0 for _ in range(num+1)]]
add_sum = [[0 for _ in range(num+1)] for _ in range(num+1)]
answers = []

for _ in range(num):
    numbers.append([0] + list(map(int, r().split())))

for i in range(1, num+1):
    for j in range(1, num+1):
        add_sum[i][j] = add_sum[i-1][j] + add_sum[i][j-1] - add_sum[i-1][j-1] + numbers[i][j]

for _ in range(add_num):
    start, end, start2, end2 = map(int, r().split())
    answers.append(add_sum[start2][end2] - add_sum[start-1][end2] - add_sum[start2][end-1] + add_sum[start-1][end-1])

for answer in answers:
   print(answer)
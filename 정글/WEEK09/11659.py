#구간 합 구하기 4
import sys
from collections import Counter, defaultdict
r = sys.stdin.readline

num, add_num = map(int, r().split())
numbers = [0] + list(map(int, r().split()))
add_sum = [0]
answers = []
for i in range(num):
    add_sum.append(add_sum[i] + numbers[i+1])

#print(add_sum)

for _ in range(add_num):
    start, end = map(int, r().split())
    answers.append(add_sum[end]-add_sum[start-1])

for answer in answers:
    print(answer)
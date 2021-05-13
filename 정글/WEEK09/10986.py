# 나머지 합
import sys
from collections import Counter, defaultdict
r = sys.stdin.readline

num, divide = map(int, r().split())
numbers = list(map(int, r().split()))
cnt = defaultdict(int)
numbers[0] %= divide
cnt[numbers[0]] = 1
answer = 0
for i in range(1, num):
    numbers[i] += numbers[i-1]
    numbers[i] %= divide
    cnt[numbers[i]] += 1

answer += cnt[0]
for j in range(divide):
    count = cnt[j]
    answer += count * (count -1) / 2

print(int(answer))
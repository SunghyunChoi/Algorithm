# 요세푸스 순열 문제
# n개의 원소들 중에 k번째 원소들을 계속해서 지워나간다.
# 지워지는 순서를 구하라.

import sys
from collections import deque
r = sys.stdin.readline

n, k = map(int, r().split())
arr = list(range(1,n+1))
i = 0
answer = []
while arr:
    
    i += k-1
    if i > len(arr)-1:
        #print(i, len(arr))
        i = i % len(arr)
    answer.append(arr.pop(i))

print(f"<{', '.join(list(map(str, answer)))}>")


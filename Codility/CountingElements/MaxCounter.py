# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import defaultdict

def solution(N, A):
    # write your code in Python 3.6
    maxCount = 0
    curMax = 0
    addNum = defaultdict(int)

    for num in A:
        if num > N:
            curMax = maxCount
            addNum = defaultdict(lambda: curMax)
            continue
        else:
            addNum[num] += 1
            maxCount = max(addNum[num],maxCount)
    
    answer = [curMax for _ in range(N)]
    for key, value in addNum.items():
        answer[key-1] = addNum[key]
    
    return answer

print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
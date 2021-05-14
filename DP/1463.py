#1로 만들기
#3으로 나누거나 2로 나누거나 1을 빼는 행위를 반복하여 1로 만들려고 한다.
#최소 실행 횟수를 구하라.


import sys
r = sys.stdin.readline


def solution(target):
    num = [target for _ in range(target+1)]
    num[0] = 0
    num[1] = 0

    for i in range(2, target+1):
        answer = target
        if i % 3 == 0:
            answer = num[i//3] + 1
        if i % 2 == 0:
            answer = min(answer, num[i//2] + 1)
        answer = min(answer, num[i-1]+1)
        num[i] = answer

    print(num[target])
    
if __name__=='__main__':
    target = int(r())
    solution(target)
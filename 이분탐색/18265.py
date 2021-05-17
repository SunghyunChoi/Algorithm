#MooBuzz

#순차적으로 숫자를 외치되, 3의 배수와 5의 배수일 때는 moo라고 외치는 게임이 있다.
#N번째 외쳐지는 숫자를 찾아라.

import sys
r = sys.stdin.readline

def findCalledNum(x):
    
    threeMoo = x//3
    fiveMoo = x//5
    fivteenMoo = x//15

    return x-threeMoo-fiveMoo+fivteenMoo

def solution():
    n = int(r())
    left = n
    right = 2*n
    answer = 0

    while left<=right:
        mid = (left+right)//2
        result = findCalledNum(mid)
        if result > n:
            right = mid-1
        elif result < n:
            left = mid+1
        else:
            while mid%3==0 or mid%5==0:
                mid -= 1
            answer = mid
            break
    
    print(answer)

if __name__=='__main__':
    solution()

#괄호의 값

import sys
r = sys.stdin.readline

def getNum(num, openClose):
    for p in openClose:
        if p == '(':
            num *= 2
        else:
            num *= 3
    return num

def solution(string):
    answer = 0
    openClose = []

    while string:
        char = string.pop()
        if char == ')':
            try:
                if string[-1] == '(':
                    string.pop()
                    answer += getNum(2, openClose)
                else:
                    openClose.append('(')
            except:
                return 0
        elif char == ']':
            try:
                if string[-1] == '[':
                    string.pop()
                    answer += getNum(3, openClose)
                else:
                    openClose.append('[')
            except:
                return 0
        elif char == '(':
            try:
                nextClose = openClose.pop()
                if nextClose != char:
                    return 0
            except:
                return 0
        else:
            try:
                nextClose = openClose.pop()
                if nextClose != char:
                    return 0
            except:
                return 0
    if openClose:
        return 0
    return answer


if __name__=='__main__':
    string = list(r().strip())
    print(solution(string))


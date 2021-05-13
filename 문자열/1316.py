#같은 문자열끼리 뭉쳐있는지 확인

import sys
r = sys.stdin.readline

def isGrouped(string):
    charSet = set()
    checkIdx = 0
    newChar = string[checkIdx]
    charSet.add(newChar)
    checkIdx += 1

    while checkIdx < len(string):
        nextChar = string[checkIdx]
        if nextChar == newChar:
            checkIdx += 1
            continue
        if nextChar in charSet:
            return False
        else:
            charSet.add(nextChar)
            newChar = nextChar
            checkIdx += 1
    
    return True

if __name__=='__main__':
    
    strNum = int(r())
    answer = 0

    for _ in range(strNum):
        if isGrouped(r().strip()):
            answer += 1
    print(answer)
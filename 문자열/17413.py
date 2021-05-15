#단어 뒤집기 2

import sys
from collections import deque
r = sys.stdin.readline

def solve():
    oldString = list(r().strip())
    strLen = len(oldString)
    oldString.append('<')
    newString = []
    idx = 0

    while idx < strLen:
        if oldString[idx] == '<':
            while True:
                if oldString[idx]=='>':
                    newString.append(oldString[idx])
                    idx += 1
                    break
                newString.append(oldString[idx])
                idx += 1
        stk = deque([])
        while oldString[idx] not in ['<', ' ']:
            stk.append(oldString[idx])
            idx += 1
        while stk:
            newString.append(stk.pop())
        if oldString[idx]==' ':
            newString.append(' ')
            idx += 1

    print(''.join(newString))

if __name__=='__main__':
    solve()
#소수경로

import math
import sys
import sys
sys.setrecursionlimit(10**7)

r = sys.stdin.readline
answer = float('inf')
answerList = []

def isPrime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if not n%i:
            return False
    return True


def findPrime(x, findNum, depth, primeBool, visited, lastChecked):
    global answer
    if x==findNum:
        answer = min(answer, depth)
        return

    def iterCheck(x, findNum, checkIdx, start, end, interval):    
        listX = list(str(x))
        for i in range(start, end, interval):
            listX[checkIdx] = str(i)
            newX = int(''.join(listX))
            if not visited[newX] and primeBool[newX]:
                # print(newX)
                visited[newX] = 1
                findPrime(newX, findNum, depth+1, primeBool, visited, checkIdx)
                visited[newX] = 0
                
    if lastChecked!= 0:
        iterCheck(x, findNum, 0, 1, 10, 1)
    if lastChecked!= 1:
        iterCheck(x, findNum, 1, 0, 10, 1)
    if lastChecked!= 2:
        iterCheck(x, findNum, 2, 0, 10, 1)
    if lastChecked!= 3:
        iterCheck(x, findNum, 3, 1, 9, 2)

    return

testCase = int(r())
primeBool = [0 for _ in range(10000)]
for i in range(1000, 10000):
    primeBool[i] = isPrime(i)

for _ in range(testCase):
    oldPwd, newPwd = map(int, r().strip().split())
    visited = [0 for _ in range(10000)]
    visited[oldPwd] = 1
    findPrime(oldPwd, newPwd, 0, primeBool, visited, 10)
    if answer == float('inf'):
        print('impossible')
    else:
        print(answer)
        answer = float('inf')


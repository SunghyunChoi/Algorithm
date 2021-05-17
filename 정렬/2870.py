import sys
r = sys.stdin.readline

def returnMax(string):
    parseNums = []
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    parseNum = ''
    for char in string:
        if char in num:
            parseNum += char
        else:
            if parseNum:
                parseNums.append(int(parseNum))
                parseNum = ''
    #마지막에 남아있는 경우 추가
    if parseNum:
        parseNums.append(int(parseNum))

    return parseNums

def solution():
    testCase = int(r())
    answerList = []
    for _ in range(testCase):
        answerList.extend(returnMax(r().strip()))
    answerList = sorted(answerList)
    for answer in answerList:
        print(answer)

if __name__=='__main__':
    solution()
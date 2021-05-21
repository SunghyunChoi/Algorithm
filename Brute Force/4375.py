import sys
r = sys.stdin.readline

while True:
    inputNum = r()
    if inputNum=='\n':
        break
    #이미 1로만 이루어진 경우 길이를 출력한다.
    if set(list(inputNum)) == {'1'}:
        len(inputNum)
        continue

    testNum = 1
    k = 1
    try:
        inputNum = int(inputNum)
    except:
        break
    while True:
        if testNum%inputNum:
           testNum = testNum * 10 + 1
           testNum %= inputNum
           k += 1
           continue
        break
    print(k) 
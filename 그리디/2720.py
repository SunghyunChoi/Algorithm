#세탁소 사장 동혁
#최소 동전 개수로 거스름돈을 주자.

import sys
r = sys.stdin.readline

def solve(change, answer):
    quater = 0
    dime = 0
    nikel = 0
    penny = 0
    quater = change//25
    change -= quater*25
    dime = change//10
    change -= dime*10
    print(change)
    nikel = change//5
    change -= nikel*5
    penny = change

    answer.append((quater, dime, nikel, penny))

if __name__=='__main__':
    testCase = int(r())
    answer = []
    for _ in range(testCase):
        solve(int(r()), answer)
    for ans in answer:
        print(*ans)

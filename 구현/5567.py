

import sys
# import os
from collections import deque

r = sys.stdin.readline
# inputFilePath = os.path.abspath(os.path.curdir) + r'\구현\input\5567.txt'

def solution():
    answer = 0
    totalNum = int(r())
    inputCount = int(r())
    friendShip = [[] for _ in range(totalNum+1)]
    visited = [False for _ in range(totalNum+1)]

    # Mark FriendShip
    for _ in range(inputCount):
        friendA, friendB = map(int, r().rstrip().rsplit())
        friendShip[friendA].append(friendB)
        friendShip[friendB].append(friendA)

    relations = deque([1])
    visited[1] = True
    friendLevel = 0
    while relations and friendLevel < 3:
        level = len(relations)
        for _ in range(level):
            friend = relations.popleft()
            answer += 1
            for nextFriend in friendShip[friend]:
                if not visited[nextFriend]:
                    relations.append(nextFriend)
                    visited[nextFriend] = True
        friendLevel += 1
    
    return answer-1

if __name__=='__main__':
    # inputString = ''
    # with open(inputFilePath, 'r') as fin:
    #     inputString = fin.read()
    # print(inputString)
    print(solution())
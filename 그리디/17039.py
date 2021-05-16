#Sleepy Cow Herding

import sys
r = sys.stdin.readline

def solve():
    pos = sorted(list(map(int, r().strip().split())))
    distance = []
    distA = pos[1] - pos[0]
    distB = pos[2] - pos[1]
    if distA==distB==1:
        print(0)
        print(0)
        return
    if distA:
        distance.append(distA)
    if distB:
        distance.append(distB)

    if min(distance)==2:
        print(1)
    else:
        print(2)
    print(max(distance)-1)

if __name__=='__main__':
    solve()
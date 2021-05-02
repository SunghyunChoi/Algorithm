import sys
r = sys.stdin.readline

def okToCut(lanCables, length, N):
    countCable = 0
    for lanCable in lanCables:
        countCable += lanCable // length
        if countCable >= N:
            return True
    return False


if __name__ == '__main__':

    K, N = map(int, r().strip().split())
    sumLen = 0
    lanCables = []
    answer = 0
    for _ in range(K):
        lanCable = int(r())
        sumLen += lanCable
        lanCables.append(lanCable)

    left = 1
    right = sumLen // N

    while left <= right:
        mid = (left + right) // 2
        if okToCut(lanCables, mid, N):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    print(answer)
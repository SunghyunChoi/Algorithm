import sys
r = sys.stdin.readline

cardNum, target = map(int, r().split())
cards = sorted(list(map(int, r().split())))

start = 0
end = len(cards) - 2
answer = 0

for i in range(start, end):
    for j in range(i+1, end+1):
        for k in range(j+1, end+2):
            # testNumFinal = testNum + cards[k]
            testNumFinal = cards[i] + cards[j] + cards[k]
            if testNumFinal <= target and testNumFinal > answer:
                answer = testNumFinal

print(answer)
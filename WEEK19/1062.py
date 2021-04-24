#DP
import sys
r = sys.stdin.readline

wordNum, teachNum = map(int, r().strip().split())
teachNum -= 5
words = [r().strip() for _ in range(wordNum)]

# print(words)
needToLearn = []
answer = 0
mustLearn = {'a', 'n', 't', 'i', 'c'}
for word in words:
    needToLearn.append(set(word[4:-4]) - mustLearn)
needToLearn = sorted(needToLearn, key=lambda x: len(x), reverse = True)
# print(needToLearn, type(needToLearn))

while needToLearn and teachNum >= len(needToLearn[-1]):
    okToLearn = needToLearn[-1]
    for i in range(len(needToLearn)):
        needToLearn[i] = needToLearn[i] - okToLearn
    teachNum -= len(okToLearn)
    needToLearn.pop()
    answer += 1
    needToLearn = sorted(needToLearn, key=lambda x: len(x), reverse = True)
    while(needToLearn and len(needToLearn[-1])==0):
        needToLearn.pop()
        answer += 1
print(answer)
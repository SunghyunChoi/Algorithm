#Greedy
import sys
r = sys.stdin.readline

a = 300
b = 60
c = 10
answer = []
time = int(r())

if time%c:
    print(-1)
else:
    answerA = time//a
    answer.append(answerA)
    time -= answerA * a
    answerB = time//b
    answer.append(answerB)
    time -= answerB * b
    answerC = time//c
    answer.append(answerC)

print(*answer)
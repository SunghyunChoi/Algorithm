## 괄호의 값
## ]는 *3 )는 2로 계산하라

import sys
r = sys.stdin.readline

string = list(r().strip())
t_end = 0
s_end = 0

factor = 1
answer = 0

while string:
    x = string.pop()
    #print(x)
    if x == ']':
        t_end += 1
        factor *= 3
        if string[-1] == '[':
            string.pop()
            t_end -= 1
            answer += factor
            factor = factor // 3
    elif x == ')':
        s_end += 1
        factor *= 2
        if string[-1] == '(':
            string.pop()
            s_end -= 1
            answer += factor
            factor = factor // 2
    elif x == '(':
        s_end -= 1
        factor = factor // 2
    else:
        t_end -= 1
        factor = factor // 3

    #닫기 괄호가 먼저 시작된 경우
    if t_end < 0 or s_end < 0:
        break

if t_end==0 and s_end==0:
    print(answer)
else:
    print(0)
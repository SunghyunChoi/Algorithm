import sys
r = sys.stdin.readline

n = int(r())
# (이면 start + 1
# )이면 end + 1
# end 가 0보다 작아지면 No를 출력한다.
for i in range(n):
    string = list(r().strip())
    end = 0

    for i in range(len(string)):
        x = string.pop()
        if x == ')':
            end += 1
        else:
            end -= 1
        if end <0:
            break
    if end !=0:
        print('NO')
    else:
        print('YES')
    
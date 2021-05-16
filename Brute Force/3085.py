#사탕 게임
#인접한 다른 색의 사탕의 위치를 바꿨을 때, 열 혹은 행에서 연속된 같은 색 사탕의 최대 개수를 구한다.

import sys
r = sys.stdin.readline

def solve():
    n = int(r())
    maps = [list(r().strip()) for _ in range(n)]
    answer = 0

    #가로방향 테스트
    for i in range(n):
        for j in range(n):
            idx = j
            color = maps[i][idx]
            count = 0
            joker = 0

            if idx < n-1 and maps[i][idx+1] != color:
                if i>0 and maps[i-1][idx]==maps[i][idx+1]:
                    color = maps[i-1][idx]
                    count += 2
                    joker = 1
                    idx += 2
                    
                elif i<n-1 and maps[i+1][idx]==maps[i][idx+1]:
                    color = maps[i+1][idx]
                    joker = 1
                    idx += 2
                    count += 2

            while idx < n:
                if maps[i][idx] != color:
                    if joker == 0:
                        if i>0 and maps[i-1][idx]==color:
                            count += 1
                            joker = 1
                            idx += 1
                            continue
                        if i<n-1 and maps[i+1][idx]==color:
                            count += 1
                            joker = 1
                            idx += 1
                            continue
                        if idx < n-1 and maps[i][idx+1]==color:
                            count += 1
                            break
                        break
                    else:
                        break
                count += 1
                idx += 1
            answer = max(answer, count)

    #세로방향 검사
    for i in range(n):
        for j in range(n):
            idx = i
            color = maps[idx][j]
            count = 0
            joker = 0

            if idx < n-1 and maps[idx+1][j] != color:
                if j>0 and maps[idx][j-1]==maps[idx+1][j]:
                    color = maps[idx][j-1]
                    count += 2
                    joker = 1
                    idx += 2
                
                elif j<n-1 and maps[idx][j+1]==maps[idx+1][j]:
                    color = maps[idx][j+1]
                    joker = 1
                    idx += 2
                    count += 2

            while idx < n:
                if maps[idx][j] != color:
                    if joker == 0:
                        if j>0 and maps[idx][j-1]==color:
                            count += 1
                            idx += 1
                            joker = 1
                            continue
                        if j<n-1 and maps[idx][j+1]==color:
                            count += 1
                            idx += 1
                            joker = 1
                            continue
                        if idx < n-1 and maps[idx+1][j]==color:
                            count += 1
                            break
                        break
                    else:
                        break
                count += 1
                idx += 1
            answer = max(answer, count)

    print(answer)

if __name__=='__main__':
    solve()
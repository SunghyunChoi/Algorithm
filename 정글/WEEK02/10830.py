## 행렬제곱
## 행렬 A를 B번 제곱값을 return해라
## 행렬 A에 1000 이상인 원소가 있을 경우 나머지를 출력해라.

import sys
r = sys.stdin.readline

def arr_pow(a, b):
    answer = [[0 for _ in range(len(a[0]))] for _ in range(len(a))]
    
    if b==1:
        u_m = [[0 for _ in range(len(a))] for _ in range(len(a))]
        for i in range(len(u_m)):
            u_m[i][i] = 1       
        return arr_mul(a,u_m)
    x = arr_pow(a, b//2)
    
    if b%2:
        return arr_mul(arr_mul(x,x),a)
    else:
        return arr_mul(x,x)

def arr_mul(a, b):
    
    answer = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            for k in range(len(a[i])):
                answer[i][j] += (a[i][k] * b[k][j])
            if answer[i][j] >=1000:
                answer[i][j] = answer[i][j] % 1000
    return answer

n, b = map(int, r().split())
x = [list(map(int, r().split())) for _ in range(n)]

ans = arr_pow(x, b)
for i in range(len(ans)):
    for j in range(len(ans[0])):
        print(ans[i][j], end=' ')
    print()
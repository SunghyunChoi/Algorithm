import sys
r = sys.stdin.readline

n = int(r())
answer = []
def dfs(x, n, arr):
    if x == n:
        answer.append([k for k in arr])
        return
    for i in range(n):
        if i+1 in arr:
            continue
        arr[x] = i+1
        dfs(x+1, n, arr)
        arr[x] = 0

arr = [0 for _ in range(n)]
dfs(0, n, arr)
for ans in answer:
    print(*ans)
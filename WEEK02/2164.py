import sys
from collections import deque
r = sys.stdin.readline

n = int(r())
que = deque(list(range(1,n+1)))

while len(que) > 1:
    que.popleft()
    que.append(que.popleft())

print(que.pop())
import sys

n = int(sys.stdin.readline())
ar = []
answer = [0,0]
for i in range(n):
    ar.append(list(map(int, sys.stdin.readline().split())))
    
def check(a, start, end):
    s_c = a[start[0]][start[1]]
    e_c = a[end[0]][end[1]]
    if s_c == e_c:
        for i in range(start[0], end[0]+1):
            for j in range(start[1], end[1]+1):
                #print(a[i][j])
                if s_c == a[i][j]:
                    continue
                else:
                    #print(1, start, end, -1)
                    return -1
    else:
        #print(2, start, end, -1)
        return -1
    #print(3, start, end, s_c)
    return s_c

def cut(a, start, end):
    color = check(a, start, end)
    if color != -1:
        answer[color] += 1
        #print('add', answer)
    else:
        cut(a, start, [(start[0]+end[0])//2, (start[1] + end[1])//2])
        cut(a, [start[0], (start[1] + end[1])//2+1], [(start[0] + end[0])//2, end[1]])
        cut(a, [(start[0]+end[0])//2+1, start[1]], [end[0], (start[1] + end[1])//2])
        cut(a, [(start[0]+end[0])//2+1,(start[1]+end[1])//2+1], end)
        
cut(ar, [0,0], [n-1,n-1])

print(answer[0])
print(answer[1])
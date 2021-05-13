import sys
r = sys.stdin.readline

while(True):
    a, *b = (r().strip().split())
    a = int(a)
    if(a==0):
        break
    b = list(map(int, b))

    for i in range(a-5):
        for j in range(i+1, a):
            for k in range(j+1, a):
                for p in range(k+1, a):
                    for q in range(p+1, a):
                        for s in range(q+1, a):
                            print(b[i], b[j], b[k], b[p], b[q], b[s], end=' ')
                            print()
    print()


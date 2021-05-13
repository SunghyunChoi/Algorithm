a, b, c = map(int, input().split())
answer = 0

def get(a, b, c):
    if b==0:
        return 1
    x = get(a, b//2, c)
    
    if b%2:
        return (x * x * a) % c
    else:
        return (x * x) % c

print(get(a,b,c))

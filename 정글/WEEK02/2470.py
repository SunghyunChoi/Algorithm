import sys

n = 5 #int(sys.stdin.readline())
arr = [-99, -94, -92] #list(map(int, sys.stdin.readline().split()))
arr.sort()
print(arr)
l = 0
r = len(arr)-1
mn = float('inf')
_mn = [0,0]

while(l<r):
    
    x = arr[l] + arr[r]
    _x = abs(x)
    #print(arr[l],arr[r])
    if x > 0:
        if _x < mn:
            mn = _x
            _mn = [arr[l],arr[r]]
        r -= 1
    elif x < 0:
        if _x < mn:
            mn = _x
            _mn = [arr[l],arr[r]]
        l += 1
    else:
        mn = _x
        _mn = [arr[l],arr[r]]
        break

print(_mn[0], _mn[1])
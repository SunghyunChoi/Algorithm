## 생각나는대로 풀어보기
import sys

in_ = input#sys.stdin.readline()

s_n, a_n, l = 7, 20, 4#map(int, in_().split())
s_arr = [3, 5, 6, 10, 13, 16, 19]#list(map(int, in_().split()))
s_arr.sort()
s_arr.append(1000000000)
answer = 0

def shot(arr, x, y, k):
    
    if y>k:
        return False
    
    left = 0
    right = len(arr)-1
    
    #print(arr[left], arr[right])
    while left < right:
        center = (left + right)//2
        target = arr[center]
        
        if target > x:
            #print(1, arr[left], x, arr[right])
            right = center - 1
        elif target < x:
            #print(2, arr[left], x, arr[right])
            left = center + 1
        else:
            return True
            #print(3, arr[left], x, arr[right])
    
    l = r = 0
    if arr[left] < x:
        l = arr[left]
        r = arr[left+1]
    else:
        l = arr[left-1]
        r = arr[left]
    d = y + min(abs(x-l), abs(x-r))
    print(l, r)
    print(d)
    if k<d:
        return False
    return True        

for i in range(a_n):
    a_x, a_y = map(int, in_().split())
    t = shot(s_arr, a_x,a_y, l)
    print(t)
    if t:
        answer += 1
print(answer)
    
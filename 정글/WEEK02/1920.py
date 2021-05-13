#find 함수

def find(a, left, right, find_num):
    
    while(True):
        center = (left + right) // 2
        print(left, right, center)
        if a[center] == find_num:
            return 1
        elif a[center] < find_num:
            left = center + 1
        else:
            right = center -1
        if left > right:
            break
    return 0

n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
find_n = int(input())
find_arr = list(map(int, input().split()))

#각 입력에 대해서 있는지 확인하기

for i in find_arr:
    print(find(arr, 0, len(arr)-1, i))
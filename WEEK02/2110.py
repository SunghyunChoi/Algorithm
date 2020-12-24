n, k = 2, 2#map(int, input().split())
arr = [1,100]#[]

#for i in range(n):
#    arr.append(int(input()))
l_arr = len(arr)
arr.sort()
l = 1
    
r = arr[-1]-arr[0]

print(f"l : {l}, r : {r}")
target = 0

while l <= r:
    m = k-1
    c = (l + r)//2
    start = 0
    print("start")
    for i in range(1, l_arr):
        print(f"start : {start}, m : {m}, c : {c}")
        x = arr[i] - arr[start]
        print(x)
        if x >= c:
            print(f"{arr[i]}에 공유기를 설치합니다.")
            if m
            m -= 1
            start = i
        else:
            continue
    if m > 0:
        print(f"공유기가 {m}개 남았네. 이거보단 더 가까워져야겠다.")
        r = c-1
    else:# m < 0:
        print("공유기가 부족하네. 이거보단 더 멀어야겠다.")        
        target = c
        l = c+1
        
        

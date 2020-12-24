## 1. 모두 탐색 : O(n**2)

n = int(input())
arr = list(map(int, input().split()))
d = [0 for _ in range(len(arr))]
d[0] = 1

for i in range(1, n):
    poss = [0]
    MAX = 1
    for j in range(i-1, -1, -1):
        if arr[i]>arr[j]:
            poss.append(d[j])
    #print(arr[i], poss)
    d[i] = max(poss) + 1
        
    #print('')
    
print(max(d))
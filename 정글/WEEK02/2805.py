n,m = map(int, input().split())
tree_list = list(map(int, input().split()))
tree_list.sort()

t = len(tree_list)



def get_sum(a,t):
    total = 0
    target = 0
    for i in range(len(a)):
        #print(a[i], t)
        if t > a[i]:
            continue
        else:
            target = i
            break

    for j in range(target, len(a)):
        #print(j, target, t-1)
        total += a[j] - t
        
    return total

left = 1
right = tree_list[-1]
target = 0
while left <= right:
    center = (left + right) // 2
    x = get_sum(tree_list, center)
    #print(left,center, right, x)
    if m < x:
        left = center + 1
        target = center
    elif m > x:
        right = center - 1
    else:
        target = center
        break

        
print(target)
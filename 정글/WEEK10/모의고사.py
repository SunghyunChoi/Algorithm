def solution(answers):
    
    hit_one = 0
    hit_two = 0
    hit_three = 0
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for idx,answer in enumerate(answers):
        if one[idx%len(one)] == answer:
            hit_one += 1
        if two[idx%len(two)] == answer:
            hit_two += 1
        if three[idx%len(three)] == answer:
            hit_three += 1
    
    result = [[1, hit_one], [2, hit_two], [3, hit_three]]
    
    result = sorted(result, key=lambda x:x[1], reverse=True)
    order = []
    i = 0
    while(True):
        order.append(result[i][0])
        if i == (len(result)-1):
            break
        if result[i][1] > result[i+1][1]:
            break
        i += 1
    return order



solution([1, 3, 2, 4, 2])
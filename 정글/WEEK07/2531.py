import sys
from collections import Counter
r = sys.stdin.readline

plate_num, menu_num, eat_in_row, coupon = map(int, r().split())
plates = []
for _ in range(plate_num):
    plates.append(int(r()))


plates = plates + plates
answer = 0
eat_num = Counter(plates[:eat_in_row])
#print(plate_num, menu_num, eat_in_row, coupon, plates, eat_num)

eat_num[coupon] += 1
# i = plate_num-1 -> back to original list
for i in range(plate_num-1):
    
    if(eat_num[plates[i]] == 1):
        del eat_num[plates[i]]
    else:
        eat_num[plates[i]] -= 1
    
    eat_num[plates[eat_in_row + i]] += 1
    #print(eat_num)
    answer = max(answer, len(eat_num.keys())) 


print(answer)
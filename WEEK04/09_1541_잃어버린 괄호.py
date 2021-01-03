##잃어버린 괄호


####################  입력  ####################
import heapq
import sys
from collections import deque, defaultdict
r = sys.stdin.readline
#################################################

string = r().strip()
string = string.split('-')
string = [list(map(int,x.split('+'))) for x in string]
#print(string)

result = sum(string[0])

for i in range(1, len(string)):
    result -= sum(string[i])

print(result)
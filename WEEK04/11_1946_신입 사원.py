import sys
r = sys.stdin.readline

test_case = int(r())

for i in range(test_case):
    people_count = int(r())
    scores = []
    answer = 1
    
    for i in range(people_count):
        paper, interview = map(int, r().split())
        scores.append([paper,interview])
    scores.sort(key = lambda x : x[0])
    minimum = scores[0][1]
    
    for i in range(1, len(scores)):
        if minimum > scores[i][1]:
            minimum = scores[i][1]
            answer += 1
    print(answer)
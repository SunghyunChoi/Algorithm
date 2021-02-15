import math

def solution(progresses, speeds):
    answer = []
    end = []
    count = 1
    before_available = math.ceil((100-progresses[0])/speeds[0])
    print(before_available)
    now_available = 0
    for i in range(1, len(progresses)):
        now_available = math.ceil((100-progresses[i])/speeds[i])
        print(now_available)
        if now_available <= before_available:
            if i == (len(progresses)-1):
                count += 1
                answer.append(count)
                break
            else:
                count += 1
                continue
        else:
            answer.append(count)
            before_available = now_available
            count = 1
            if i == (len(progresses)-1):
                answer.append(count)
                break
    return answer

print(solution([5, 5, 5], [21, 25, 20]))
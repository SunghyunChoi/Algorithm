import math

def solution(n, stations, w):
    answer = 0

    start = 1
    answer += math.ceil(stations[0] - w - start/(2*w+1))
    for i in range(1, len(stations)):
        answer += math.ceil(stations[i] - stations[i-1] - 2*w - 1)
    answer += math.ceil(n - w - stations[-1]/(2*w+1))
    return answer
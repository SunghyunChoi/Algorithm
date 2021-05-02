import sys
r = sys.stdin.readline

lessonNum, blueNum = map(int, r().strip().split())
 

answer = 0

lessons = list(map(int, r().strip().split()))
left = 0
right = sum(lessons)

def testMax(x, Max):
    
    countBlue = 1
    bucket = 0
    for lesson in lessons:
        if lesson > x:
            return [False,0]
        elif bucket + lesson <= x:
            bucket += lesson
        else:
            countBlue += 1
            bucket = lesson

    if countBlue > Max:
        return [False, 0]
    return [True, countBlue]

while left<=right:
    mid = (left + right)//2
    result = testMax(mid, blueNum)
    if result[0]:
        right = mid - 1
        answer = mid
    else:
        left = mid + 1

print(answer)


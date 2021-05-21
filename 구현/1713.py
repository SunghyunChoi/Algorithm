#후보 추천하기

import sys
r = sys.stdin.readline

#새로운 추천 표를 받아 frame을 갈아야 하는지 확인한다.
def newVote(frames, vote, maxLen):
    isDisplayed = False

    #게시 시간을 1씩 늘린다(정렬 방향을 추천수와 동일하게 만들기 위해 -1씩 늘린다)
    for idx, frame in enumerate(frames):
        #이미 존재하는 경우 추천수 증가
        if vote == frame[0]:
            frames[idx][1] += 1
            isDisplayed = True
        frames[idx][2] -= 1

    if len(frames) == maxLen:
        if isDisplayed:
            return frames
        else:
            frames = sorted(frames, key=lambda x:(x[1], x[2]), reverse=True)
            frames.pop()
            frames.append([vote, 1, 0])
            return frames
    else:
        if isDisplayed:
            return frames
        else:
            frames.append([vote, 1, 0])
            return frames


def solution():
    frames = []
    frameNum = int(r())
    voteNum = int(r())
    votes = list(map(int, r().rstrip().split()))

    for vote in votes:
        frames = newVote(frames, vote, frameNum)
    
    frames = sorted(frames, key=lambda x:x[0])
    for frame in frames:
        print(frame[0], end=' ')

if __name__=='__main__':
    solution()
#국회의원 선거
import sys
r = sys.stdin.readline

def solution():
    candidateNum = int(r())
    myVote = int(r())
    votes = []
    answer = 0
    change = 1

    for _ in range(candidateNum-1):
        votes.append(int(r()))
    votes = sorted(votes, reverse=True)

    while change:
        change = 0
        for idx, vote in enumerate(votes):
            if vote >= myVote:
                votes[idx] -= 1
                myVote += 1
                answer += 1
                change += 1
                if idx < len(votes)-1 and votes[idx] < votes[idx+1]:
                    sortIdx = 0
                    while sortIdx<len(votes)-1:
                        if votes[sortIdx]<votes[sortIdx+1]:
                            swap = votes[sortIdx]
                            votes[sortIdx] = votes[sortIdx+1]
                            votes[sortIdx+1] = swap
                            sortIdx += 1
                        else:
                            break
                break

    print(answer)


if __name__=='__main__':
    solution()
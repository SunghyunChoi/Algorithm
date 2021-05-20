import sys
r = sys.stdin.readline


def solution():

    countryNum, answerIdx = map(int, r().rstrip().split())
    country = []
    rank = 1
    countryCount = 1
    for _ in range(countryNum):
        country.append(list(map(int, r().rstrip().split())))
    
    country = sorted(country, key=lambda x:(x[1], x[2], x[3]), reverse=True)

    #더미 데이터 추가
    country.append([0, 0, 0, 0])

    for idx, c in enumerate(country):
        if c[0] == answerIdx:
            print(rank)
            return
        else:
            nextCountry = country[idx+1]
            if nextCountry[1] == c[1] and nextCountry[2] == c[2] and nextCountry[3] == c[3]:
                countryCount += 1
                continue
            else:
                rank += countryCount
                countryCount = 1

if __name__=='__main__':
    solution()

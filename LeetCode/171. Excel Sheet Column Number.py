class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        factor = 1
        answer = 0
        for i in range(len(columnTitle)-1, -1, -1):
            answer += (ord(columnTitle[i]) - 64) * factor
            factor *= 26

        return answer

solution = Solution()
solution.titleToNumber('AA')



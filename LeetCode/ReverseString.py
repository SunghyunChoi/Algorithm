class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        changeCount = len(s)//2
        for i in range(changeCount):
            swap = s[i]
            s[i] = s[-1 * i -1]
            s[-1 * i - 1] = swap
        
        print(s)

s = ["h", "i"]
solution = Solution()
solution.reverseString(s)

print(s)
        
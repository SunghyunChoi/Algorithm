from collections import deque

class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroIdx = deque([])
        for idx, num in enumerate(nums):
            if num and zeroIdx:
                replaceIdx = zeroIdx.popleft()
                nums[replaceIdx] = num
                nums[idx] = 0
                zeroIdx.append(idx)
            elif num == 0:
                zeroIdx.append(idx)
                
        
solution = Solution()
a = [0]
solution.moveZeroes(a)
print(a)
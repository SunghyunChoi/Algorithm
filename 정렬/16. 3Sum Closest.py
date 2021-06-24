from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = 100000
        threeSum = 0
        nums = sorted(nums)
        answer = 0

        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1

            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]
                newDiff = abs(target - threeSum)
                if newDiff < diff:
                    diff = newDiff
                    answer = threeSum
                if threeSum < target:
                    left += 1
                elif threeSum > target:
                    right -= 1
                else:
                    return threeSum
            
        return answer
solution = Solution()
print(solution.threeSumClosest([1,2,5,10,11], 12))
from collections import defaultdict

class Solution:
    def majorityElement(self, nums) -> int:
        elemCount = defaultdict(int)
        majorityCount = len(nums)//2+1 if len(nums)%2 else len(nums)//2


        for num in nums:
            elemCount[num] += 1
            if elemCount[num] >= majorityCount:
                return num

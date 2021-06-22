from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums) -> bool:
        count = defaultdict(int)

        for num in nums:
            if count[num] != 0:
                return True
            else:
                count[num] += 1

        return False
        
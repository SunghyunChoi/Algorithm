class Solution:
    def reverseInt(self, x):
        
        mod = 0 
        result = 0

        while x:
            mod = x%10
            x //= 10
            result = result * 10 + mod

        return result

    def reverse(self, x: int) -> int:
        
        startIdx = 0
        answer = 0
        
        # Negative
        isNegative = -1 if x<0 else 1
        
        
        # Positive & Negative
        answer = self.reverseInt(x * isNegative)
        
        
        if abs(answer) >= 2**31:
            return 0
        return isNegative * answer

class Solution:
    def isPrime(self, n: int) -> int:
        countRange = int(n**(0.5))
        for i in range(2, countRange+1):
            if n%i == 0:
                return False
        return True


    def countPrimes(self, n: int) -> int:
    
        num = [1 for _ in range(n)]

        for i in range(2, int(n**(0.5))+1):
            if num[i]:
                j = 2
                while j*i < n:
                    num[j*i] = 0
                    j += 1
            
        return sum(num)-2
            


solution = Solution()
solution.countPrimes(10)
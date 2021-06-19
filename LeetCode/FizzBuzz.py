class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        answer = []
        for i in range(1, n+1):
            result = ""
            if i%3==0:
                result += "Fizz"
            if i%5==0:
                result += "Buzz"
            if not result:
                result += str(i)
            answer.append(result)
        return answer

from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        carry = 0
        nextNode1 = l1
        nextNode2 = l2
        answerStart = ListNode()
        answerNode = answerStart
        answerNext = ListNode()
        
        while True:
            value = nextNode1.val + nextNode2.val + carry
            carry = 0
            if value > 9:
                carry = 1
                value -= 10
            
            answerNext = ListNode()
            answerNode.val = value
            if nextNode1.next==None and nextNode2.next==None and carry==0:
                break
            answerNode.next = answerNext
            answerNode = answerNext
                
            if nextNode1.next:
                nextNode1 = nextNode1.next
            else:
                nextNode1.val = 0
            if nextNode2.next:
                nextNode2 = nextNode2.next
            else:
                nextNode2.val = 0
            
        return answerStart
    
solution = Solution()

a = ListNode(1, ListNode(2, ListNode(3)))
b = ListNode(1, ListNode(2, ListNode(3)))


node = solution.addTwoNumbers(a, b)
solution.printAll(node)
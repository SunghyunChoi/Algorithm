class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        beforeNode = None
        curNode = head
        if not curNode or not curNode.next:
            return head
        

        while curNode:
            nextNode = curNode.next
            curNode.next = beforeNode
            beforeNode = curNode
            curNode = nextNode
            
        return beforeNode

five = ListNode(5, None)
four = ListNode(4, five)
three = ListNode(3, four)
two = ListNode(2, three)
head = ListNode(1, two)

solution = Solution()
newHead = solution.reverseList(head)
print(newHead.next)

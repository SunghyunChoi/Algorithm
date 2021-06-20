class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def sortedArrayToBST(self, nums) -> TreeNode:
        
        left = 0
        right = len(nums)-1
        mid = (left + right) // 2
        
        root = TreeNode(nums[mid])
        
        def insertNode(nums, left, right, node):
            if left > right:
                return
            
            mid = (left + right) // 2
            newNode = TreeNode(nums[mid])
            
            if node.val < newNode.val :
                node.right = newNode
            else:
                node.left = newNode
                
            insertNode(nums, left, mid-1, newNode)
            insertNode(nums, mid+1, right, newNode)
        
        insertNode(nums, left, mid-1, root)
        insertNode(nums, mid+1, right, root)
        
        return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        answer = []
        nodeList = []
        visitNode = root
        if not root:
            return []
        def go(node):
            if node.left:
                go(node.left)
            if node.val:
                nodeList.append(node.val)
            if node.right:
                go(node.right)
            
        go(root)
        return nodeList 
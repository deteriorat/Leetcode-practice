# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mySum(self, root: Optional[TreeNode], nowsum) -> int:
        if root is None:
            return 0
        nowsum = nowsum*10 + root.val
        if root.left == None and root.right == None:
            return nowsum
        return self.mySum(root.left, nowsum) + self.mySum(root.right, nowsum)
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.mySum(root, 0)
        
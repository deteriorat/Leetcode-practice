# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = 0
        def dfs(root):
            if root is None: return
            dfs(root.left)
            print(root.val)
            self.k -= 1
            if self.k == 0:
                self.ans = root.val
            dfs(root.right)

            return 
        self.k = k
        dfs(root)
        return self.ans


#这里需要注意在递归python函数中的生命周期
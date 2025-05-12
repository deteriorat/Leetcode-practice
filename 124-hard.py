#需要注意maxans初始化为负无穷，主要是考察思路的bian

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_ans = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxcon(root):
            if root == None:
                return 0
            left_con = max(maxcon(root.left), 0)
            right_con = max(maxcon(root.right), 0)

            maxpath = root.val + left_con + right_con
            self.max_ans = max(self.max_ans, maxpath)

            return root.val + max(left_con, right_con)
        maxcon(root)

        return self.max_ans
        
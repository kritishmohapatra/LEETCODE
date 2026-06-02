# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec(self, root, mx):
        if not root:
            return 0
        lm=max(0, self.rec(root.left, mx))
        rm=max(0, self.rec(root.right, mx))
        mx[0]=max(mx[0], root.val+lm+rm)
        return root.val+max(lm, rm)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mx=[float("-inf")]
        self.rec(root, mx)
        return mx[0]
        
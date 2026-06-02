# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def help(self, root, d):
        if not root:
            return 0
        lh=self.help(root.left, d)
        rh=self.help(root.right, d)
        d[0]=max(d[0], lh+rh)
        return 1+max(lh, rh)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d=[0]
        self.help(root, d)
        return d[0]
        
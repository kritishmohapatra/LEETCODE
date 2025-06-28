# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root,minval,maxval):
        if root==None:
            return True
        if root.val>=maxval or root.val<=minval:
            return False
        return self.solve(root.left,minval,root.val) and self.solve(root.right,root.val,maxval)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.solve(root,float("-inf"),float("inf"))
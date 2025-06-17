# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root):
        if root==None:
            return 0
        lh=self.dfs(root.left)
        if lh==-1:
            return -1
        rh=self.dfs(root.right)
        if rh==-1:
            return -1
        if (abs(lh-rh)>1):
            return -1
        return max(lh, rh)+1
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)!=-1
        
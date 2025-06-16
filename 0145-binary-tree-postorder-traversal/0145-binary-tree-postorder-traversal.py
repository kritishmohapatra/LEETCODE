# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec(self, root, ans):
        if not root:
            return
        self.rec(root.left, ans)
        self.rec(root.right, ans)
        ans.append(root.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        self.rec(root, ans)
        return ans
        
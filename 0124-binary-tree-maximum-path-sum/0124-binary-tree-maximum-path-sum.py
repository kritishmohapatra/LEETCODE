# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec(self, root, maxi):
        if not root:
            return 0
        lmp=max(0, self.rec(root.left,maxi))
        rmp=max(0, self.rec(root.right,maxi))
        maxi[0]=max(maxi[0], lmp+rmp+root.val)
        return root.val+max(lmp, rmp)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi=[float("-inf")]
        self.rec(root, maxi)
        return maxi[0]
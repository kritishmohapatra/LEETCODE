# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root,c,k,ks):
        if not root or c[0]>=k:
            return
        self.inorder(root.left,c,k,ks)
        c[0]+=1
        if c[0]==k:
            ks[0]=root.val
            return
        self.inorder(root.right,c,k,ks)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ks=[-1]
        c=[0]
        self.inorder(root,c,k,ks)
        return ks[0]

        
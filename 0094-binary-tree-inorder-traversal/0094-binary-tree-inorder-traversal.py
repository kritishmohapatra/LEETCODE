# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def ino(self, root, arr):
        if not root:
            return
        self.ino(root.left, arr)
        arr.append(root.val)
        self.ino(root.right, arr)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr=[]
        self.ino(root, arr)
        return arr
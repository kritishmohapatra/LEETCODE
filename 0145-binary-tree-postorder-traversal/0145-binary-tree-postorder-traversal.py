# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pos(self, root, arr):
        if not root:
            return
        self.pos(root.left, arr)
        self.pos(root.right, arr)
        arr.append(root.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr=[]
        self.pos(root, arr)
        return arr
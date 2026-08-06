# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pre(self, arr, root):
        if not root:
            return 
        arr.append(root.val)
        self.pre(arr, root.left)
        self.pre(arr, root.right)  
            
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr=[]
        self.pre(arr, root)
        return arr
        
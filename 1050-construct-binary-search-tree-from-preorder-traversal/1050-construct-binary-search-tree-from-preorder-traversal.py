# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build(self, arr,i, b):
        if self.i ==len(arr) or arr[self.i ]>b:
            return None
        val=arr[self.i]
        self.i+=1
        root=TreeNode(val)
        root.left=self.build(arr, i, root.val)
        root.right=self.build(arr, i,b)
        return root

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.i = 0 
        return self.build(preorder, self.i, float("inf"))

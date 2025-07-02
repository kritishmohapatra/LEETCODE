# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.fst=None
        self.lst=None
        self.mid=None
        self.prev=None
    def ino(self, root):
        if root is None:
            return 
        self.ino(root.left)
        if self.prev is not None and root.val<self.prev.val:
            if self.fst is None:
                self.fst=self.prev
                self.mid=root
            else:
                self.lst=root
        self.prev=root
        self.ino(root.right)
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.fst=self.lst=self.mid=None
        self.prev=TreeNode(float("-inf"))
        self.ino(root)
        if self.fst and self.lst:
            self.lst.val, self.fst.val=self.fst.val,self.lst.val
        elif self.fst and self.mid:
            self.mid.val, self.fst.val=self.fst.val,self.mid.val
        
        

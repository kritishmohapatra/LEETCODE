# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        if not root:
            return res
        q=deque()
        q.append(root)
        f=True
        while q:
            s=len(q)
            r=[0]*s
            for i in range(s):
                node=q.popleft()
                ind=i if f else (s-1-i)
                r[ind]=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            f=not f
            res.append(r)
        return res
            





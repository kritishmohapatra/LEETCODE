# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.push(root)  # <-- Needed to initialize stack with leftmost path

    def next(self) -> int:
        cur = self.stack.pop()
        self.push(cur.right)
        return cur.val

    def hasNext(self) -> bool:
        return bool(self.stack)

    def push(self, node):
        while node:
            self.stack.append(node)
            node = node.left
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
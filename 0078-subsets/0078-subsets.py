class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(i):
            if i == len(nums):
                res.append(path[:])   # copy!
                return

            # choice 1: skip
            backtrack(i + 1)

            # choice 2: take
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()   # undo

        backtrack(0)
        return res
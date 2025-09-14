class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        mini=float("inf")
        for task in tasks:
            mini=min(task[0]+task[1],mini)
        return mini
class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        pos = [val for val in nums if val >= 0]
        if not pos:
            return nums
        
        siz = len(pos)
        mod = k % siz
        rot = pos[mod:] + pos[:mod]
        
        res = []
        ptr = 0
        for val in nums:
            if val < 0:
                res.append(val)
            else:
                res.append(rot[ptr])
                ptr += 1
        return res
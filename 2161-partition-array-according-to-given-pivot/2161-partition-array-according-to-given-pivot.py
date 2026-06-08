class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        s,e,g=[], [], []
        for  n in nums:
            if n<pivot:
                s.append(n)
            elif n==pivot:
                e.append(n)
            else:
                g.append(n)
        return s+e+g
        
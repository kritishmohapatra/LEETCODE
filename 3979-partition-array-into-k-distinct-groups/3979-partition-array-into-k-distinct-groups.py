class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        if n%k!=0:
            return False
        d=Counter(nums)
        g=n//k
        for key, val in d.items():
            if val>g:
                return False
        return True        
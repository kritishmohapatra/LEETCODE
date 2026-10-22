class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums)
        def rot(arr, tar):
            for i in range(n):
                if all(arr[(i + j) % n] == tar[j]
                       for j in range(n)):
                    return i
            return -1

        inc=list(range(n))
        dec=inc[::-1]
        a=rot(nums, inc)
        b=rot(nums, dec)
        ans=float("inf")
        if a!=-1:
            ans=min(ans, a, 2+n-a if a else 0)
        if b!=-1:
            ans=min(ans, 1+b, 1+n-b)
        return ans if ans != float('inf') else -1
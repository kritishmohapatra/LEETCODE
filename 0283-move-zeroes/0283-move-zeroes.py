class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        j=-1
        for i in range(0,n):
            if nums[i]==0:
                j=i
                break
        if j==-1:
            return nums
        for i in range(j+1, n):
            if nums[i]!=0:
                (nums[j], nums[i])=(nums[i], nums[j])
                j+=1
        return nums
        
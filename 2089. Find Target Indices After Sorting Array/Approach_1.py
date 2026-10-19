class Solution:
    def targetIndices(self, arr: list[int], target: int) -> list[int]:
        arr.sort()
        ans=[]
        for i in range(len(arr)):
            if arr[i]==target:
                ans.append(i)
        return ans
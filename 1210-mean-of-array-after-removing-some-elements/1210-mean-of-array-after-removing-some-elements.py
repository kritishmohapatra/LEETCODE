class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n=len(arr)
        five=int(n/20)
        arr.sort()
        arr=arr[five:-five]
        return mean(arr)
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans=1
        low=0
        high=len(letters)-1
        while(low<=high):
            mid=(low+high)//2
            if letters[mid]>target:
                ans=letters[mid]
                high=mid-1
            else:
                low=mid+1
        if ans==1:
            return letters[0]
        return ans

        
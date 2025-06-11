class Solution:
    def trap(self, height: List[int]) -> int:
        total=0
        i=0
        j=len(height)-1
        lm=0
        rm=0
        while i<j:
            lm=max(lm, height[i])
            rm=max(rm , height[j])
            if height[i]<=height[j]:
                total+=lm-height[i]
                i+=1
            else:
                total+=rm-height[j]
                j-=1
        return total
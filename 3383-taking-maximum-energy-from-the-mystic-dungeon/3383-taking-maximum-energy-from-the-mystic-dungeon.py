class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        t=energy 
        n=len(energy)
        for i in range(n-1,-1,-1): 
            if i+k<n: 
                t[i]=energy[i]+t[i+k] 
        return max(t) 
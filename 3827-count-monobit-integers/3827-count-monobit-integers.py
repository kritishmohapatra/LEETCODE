class Solution:
    def countMonobit(self, n: int) -> int:
        ans = 0
        
        for num in range(n + 1):
            bit = bin(num)[2:]
            if len(set(bit)) == 1:
                ans += 1
        
        return ans
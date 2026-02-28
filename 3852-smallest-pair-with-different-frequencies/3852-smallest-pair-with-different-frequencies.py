class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        freq = Counter(nums)
        unique_nums = sorted(freq.keys())
        n = len(unique_nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                if freq[unique_nums[i]] != freq[unique_nums[j]]:
                    return [unique_nums[i], unique_nums[j]]
                    
        return [-1, -1]

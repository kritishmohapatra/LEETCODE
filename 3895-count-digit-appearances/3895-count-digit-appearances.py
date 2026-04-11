class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        s=""
        for x in nums:
            s+=str(x)
        c=Counter(s)
        return c[str(digit)]
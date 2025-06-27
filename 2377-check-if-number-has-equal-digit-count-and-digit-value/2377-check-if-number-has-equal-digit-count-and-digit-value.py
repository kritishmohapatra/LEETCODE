class Solution:
    def digitCount(self, num: str) -> bool:
        c=Counter(num)
        return all(c[str(i)]==int(digit) for i, digit in enumerate(num))
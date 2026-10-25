class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        x, y=a.bit_count(), b.bit_count()
        return x*y if x>=y else y//x
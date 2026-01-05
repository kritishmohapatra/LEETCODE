class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        a=start^goal
        k=bin(a).replace("0b","")
        return k.count("1")
        
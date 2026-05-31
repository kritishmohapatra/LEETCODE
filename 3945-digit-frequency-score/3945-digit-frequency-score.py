class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        s=Counter(str(n))
        sc=0
        for k, v in s.items():
            sc+=int(k)*v
        return sc
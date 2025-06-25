class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        c=Counter(s)
        return max(c.values())==min(c.values())
        
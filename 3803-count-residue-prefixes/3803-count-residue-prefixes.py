class Solution:
    def residuePrefixes(self, s: str) -> int:
        res = 0
        cur = set()
        for i, c in enumerate(s):
            cur.add(c)
            if len(cur) == (i + 1) % 3:
                res += 1
        return res
        
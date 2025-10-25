class Solution:
    def lexSmallest(self, s: str) -> str:
        ans = ""
        n = len(s)
        def upd(t):
            nonlocal ans
            if not ans:
                ans = t
            elif t < ans:
                ans = t
        for k in range(1, n + 1):
            upd(s[:k][::-1] + s[k:])
            upd(s[:k] + s[k:][::-1])
        return ans
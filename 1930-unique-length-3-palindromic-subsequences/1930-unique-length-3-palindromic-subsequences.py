class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res=set()
        left=set()
        mp=Counter(s)
        for m in s:
            mp[m]-=1
            for c in left:
                if mp[c]>0:
                    res.add((m, c))
            left.add(m)
        return len(res)

            
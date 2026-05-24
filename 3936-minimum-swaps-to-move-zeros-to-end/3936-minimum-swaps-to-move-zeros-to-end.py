class Solution:
    def minimumSwaps(self, a: list[int]) -> int:
        c = a.count(0)
        a.reverse()
        ans = 0
        for i in range(c):
            ans += a[i] != 0
        return ans
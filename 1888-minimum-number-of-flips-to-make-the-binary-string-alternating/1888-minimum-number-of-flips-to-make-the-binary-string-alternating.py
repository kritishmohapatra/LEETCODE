class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
    
        count = [[0] * 2 for _ in range(2)]

        for i, c in enumerate(s):
            count[int(c)][i % 2] += 1

        
        ans = min(count[1][0] + count[0][1], count[0][0] + count[1][1])

        for i, c in enumerate(s):
            count[int(c)][i % 2] -= 1
            count[int(c)][(n + i) % 2] += 1
            ans = min(ans, count[1][0] + count[0][1], count[0][0] + count[1][1])

        return ans 
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        tc = sum(cost)
        cc = defaultdict(int)

        for ch, c in zip(s, cost):
            cc[ch] += c

        return tc - max(cc.values())
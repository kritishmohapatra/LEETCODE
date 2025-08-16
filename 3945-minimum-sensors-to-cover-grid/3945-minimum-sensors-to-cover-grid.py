class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        side=2*k+1
        return math.ceil(n/side)*math.ceil(m/side)
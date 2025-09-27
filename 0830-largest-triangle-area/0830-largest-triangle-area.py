class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        ans=0
        for ax, ay in points:
            for bx, by in points:
                for cx, cy in points:
                    ans=max(ans, 0.5*abs((bx-ax)*(cy-ay)-(cx-ax)*(by-ay)))
        return ans
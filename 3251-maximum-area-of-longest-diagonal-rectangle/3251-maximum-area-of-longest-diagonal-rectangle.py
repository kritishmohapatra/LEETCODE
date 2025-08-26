class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_area, max_diag=0,0
        for l, w in dimensions:
            curr=l*l+w*w
            if curr>max_diag or (curr==max_diag and l*w >max_area):
                max_diag=curr
                max_area=l*w
        return max_area
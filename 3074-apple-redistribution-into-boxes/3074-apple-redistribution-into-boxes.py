class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        ap=sum(apple)
        cs=0
        for i, c in enumerate(sorted(capacity, reverse=True)):
            cs+=c
            if cs>=ap:
                return i+1
        return len(capacity)
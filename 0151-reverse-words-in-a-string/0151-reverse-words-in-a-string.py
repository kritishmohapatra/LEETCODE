class Solution:
    def reverseWords(self, s: str) -> str:
        k=s.split()
        k.reverse()
        p=" ".join(k)
        return p
        
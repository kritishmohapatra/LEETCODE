class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s=set([c for c in word if c.islower()])
        p=set([k.lower() for k in word if k.isupper()])
        return len(s&p)
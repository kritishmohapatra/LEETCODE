class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ans=0
        s=set(brokenLetters)
        for word in text.split():
            ans+=all(c not in s for c in word)
        return ans
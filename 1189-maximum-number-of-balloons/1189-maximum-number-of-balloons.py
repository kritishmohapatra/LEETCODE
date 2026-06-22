from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countext={k:0 for k in "balon"}
        for c in text:
            if c in countext:
                countext[c]+=1
        countext["l"]//=2
        countext["o"]//=2
        return min(countext.values())

        
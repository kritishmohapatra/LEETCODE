class Solution:
    def generateTag(self, caption: str) -> str:
        words=caption.split()
        if not words:
            return "#"
        cw=[words[0].lower()]+[w.capitalize() for w in words[1:]]
        co="#"+"".join(cw)
        fi="#"+"".join(c for c in co[1:] if c.isalpha())
        return fi[:100]


        
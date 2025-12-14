class Solution:
    def reverseWords(self, s: str) -> str:
        v=set("aeiou")
        w=s.split()
        c=sum(ch in v for ch in w[0])
        for i in range(1, len(w)):
            if sum(ch in v for ch in w[i])==c:
                w[i]=w[i][::-1]
        return " ".join(w)
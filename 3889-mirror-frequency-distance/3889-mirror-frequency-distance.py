class Solution:
    def mirrorFrequency(self, s: str) -> int:
         
        freq = [0] * 36

        for ch in s:
            if 'a' <= ch <= 'z':
                freq[ord(ch) - ord('a')] += 1
            else:
                freq[26 + ord(ch) - ord('0')] += 1

        ans = 0

        for i in range(13):
            ans += abs(freq[i] - freq[25 - i])

        for i in range(5):
            ans += abs(freq[26 + i] - freq[26 + 9 - i])

        return ans
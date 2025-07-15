class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        vowel, consonant, vowelset=0,0,"aeiouAEIOU"
        for char in word:
            if char.isalpha():
                if char in vowelset:
                    vowel+=1
                else:
                    consonant+=1
            elif not char.isdigit():
                return False
        return vowel>=1 and consonant>=1
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        res=[]
        mapping={"2":"abc","3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs","8":"tuv", "9":"wxyz"}
        temp=deque()
        def back(idx, digit, temp, mapping):
            if idx>=len(digit):
                res.append("".join(temp))
                return 

            char=digits[idx]
            s=mapping[char]
            for i in range(0, len(s)):
                temp.append(s[i])
                back(idx+1, digits, temp, mapping)
                temp.pop()
        back(0, digits, temp, mapping)
        return res
        




        

        
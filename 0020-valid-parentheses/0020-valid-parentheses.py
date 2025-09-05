class Solution:
    def isValid(self, s: str) -> bool:
        def match(a, b):
            if a=="(" and b==")":
                return 1
            if a=="{" and b=="}":
                    return 1
            if a=="[" and b=="]":
                    return 1
            
        stack=[]
        for i in range(0, len(s)):
            if s[i]=="(" or s[i]=="{" or s[i]=="[":
                stack.append(s[i])
            elif s[i]==")" or s[i]=="}" or s[i]=="]":
                if len(stack)==0:
                    return False
                else:
                    poped=stack.pop()
                    if not(match(poped, s[i])):
                        return False
        if len(stack)==0:
            return True
        else:
            return False
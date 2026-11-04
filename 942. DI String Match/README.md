# 942. DI String Match

### Difficulty: Easy

## Description
A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:


	s[i] == 'I' if perm[i] < perm[i + 1], and
	s[i] == 'D' if perm[i] > perm[i + 1].


Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.

 
Example 1:
Input: s = "IDID"
Output: [0,4,1,3,2]
Example 2:
Input: s = "III"
Output: [0,1,2,3]
Example 3:
Input: s = "DDI"
Output: [3,2,0,1]

 
Constraints:


	1 <= s.length <= 105
	s[i] is either 'I' or 'D'.

## Submission Details
- **Status**: Accepted
- **Runtime**: 2
- **Memory**: 19820000
- **Language**: python3

## Code
```python3
class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        l=0
        h=len(s)
        ans=[]
        for ch in s:
            if ch=="I":
                ans.append(l)
                l+=1
            else:
                ans.append(h)
                h-=1
        ans.append(l)
        return ans
```

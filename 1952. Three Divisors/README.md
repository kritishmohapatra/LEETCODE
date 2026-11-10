# 1952. Three Divisors

### Difficulty: Easy

## Description
Given an integer n, return true if n has exactly three positive divisors. Otherwise, return false.

An integer m is a divisor of n if there exists an integer k such that n = k * m.

 
Example 1:


Input: n = 2
Output: false
Explantion: 2 has only two divisors: 1 and 2.


Example 2:


Input: n = 4
Output: true
Explantion: 4 has three divisors: 1, 2, and 4.


 
Constraints:


	1 <= n <= 104

## Submission Details
- **Status**: Accepted
- **Runtime**: 0 ms
- **Memory**: 18744000
- **Language**: python3

## Code
```python3
class Solution:
    def isThree(self, n: int) -> bool:
        r=int(n**0.5)
        if r*r!=n:
            return False
        if r<2:
            return False
        for i in range(2, int(r**0.5)+1):
            if r%i==0:
                return False
        return True
```

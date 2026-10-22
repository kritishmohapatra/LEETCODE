# 3942. Minimum Operations to Sort a Permutation

### Difficulty: Medium

## Description
You are given an integer array nums of length n, where nums is a permutation of the integers from 0 to n - 1.

You may perform only the following operations:


	Reverse the entire array.
	Rotate Left by One: Move the first element to the end of the array, and rest elements to left by one position.


Return an integer denoting the minimum number of operations required to sort the array in increasing order. If it is not possible to sort the array using only the given operations, return -1.

 
Example 1:


Input: nums = [0,2,1]

Output: 2

Explanation:


	Rotate Left by one: [2, 1, 0]
	Reverse the array: [0, 1, 2]


The array becomes sorted in 2 operations, which is minimal


Example 2:


Input: nums = [1,0,2]

Output: 2

Explanation:


	Reverse the array: [2, 0, 1]
	Rotate Left by one: [0, 1, 2]


The array becomes sorted in 2 operations, which is minimal.


Example 3:


Input: nums = [2,0,1,3]

Output: -1

Explanation:

It is impossible to reach [2, 0, 1, 3]. Thus, the answer is -1.


 
Constraints:


	1 <= n == nums.length <= 105
	0 <= nums[i] <= n - 1
	nums is a permutation of integers from 0 to n - 1.

## Submission Details
- **Status**: Accepted
- **Runtime**: 633
- **Memory**: 31140000
- **Language**: python3

## Code
```python3
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums)
        def rot(arr, tar):
            for i in range(n):
                if all(arr[(i + j) % n] == tar[j]
                       for j in range(n)):
                    return i
            return -1

        inc=list(range(n))
        dec=inc[::-1]
        a=rot(nums, inc)
        b=rot(nums, dec)
        ans=float("inf")
        if a!=-1:
            ans=min(ans, a, 2+n-a if a else 0)
        if b!=-1:
            ans=min(ans, 1+b, 1+n-b)
        return ans if ans != float('inf') else -1
```
